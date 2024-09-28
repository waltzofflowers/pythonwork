--Calculate for each pair of friends how many mutual friends they have. Name the columns as friend1, friend2 and num_mutual_friends.
-- name, id, friend_id
SELECT F1.name, F3.name, COUNT(*) num_mutual_friends FROM friends AS F1 JOIN friends AS F2 ON F1.friend_id = F2.friend_id JOIN friends AS F3 ON F2.friend_id = F3.id
WHERE F1.name <> F2.name AND F2.name <> F3.name AND F1.name <> F3.name
GROUP BY F1.name, F3.name
order by COUNT(*) DESC, F1.name;

--First, Add to all scooter prices in the shop the overall average price.
--Then, Calculate the average price for each brand, considering only good and original scooters (i.e., scooters with a model name and lights).
--The result should include the brand and the average price - avg_price. Sort the results by the average price in ascending order.

WITH CTE AS (
SELECT MODEL, BRAND, LIGHTS, PRICE + (SELECT AVG(PRICE) FROM SCOOTERS) AS PRICE FROM SCOOTERS
WHERE (MODEL != NULL OR MODEL != '') AND LIGHTS = 1
)

SELECT BRAND AS brand,AVG(PRICE) AS avg_price FROM CTE
GROUP BY BRAND
ORDER BY AVG(PRICE) ASC;

-- Return the top 5 customers who have spent the most on all of their orders.
-- orders: id customer_id
-- products: id price units_in_stock
--order_items: id order_id product_id quantity
-- PSQL ZZZ(EXPECTED MSSQL...)
SELECT O2.customer_id, SUM(P.price * O1.quantity) AS total_spending 
FROM order_items AS O1 
LEFT JOIN orders AS O2 
ON O1.order_id = O2.id
INNER JOIN products AS P
ON P.id = O1.product_id
GROUP BY customer_id
ORDER BY total_spending DESC
LIMIT 5;


--factory: brand sugar
-- book: brand day chocolates

-- For each brand, extract the average chocolates (from the book table) that were made. Round the result to 2 decimals places,
--and extract the number of chocolates the factory can produce now (from the factory table).

--Not all of the brands are relevant. The analyst doesn't like odd numbers, so he decided to sort the brand's name in descending order and investigate only the even rows.
-- Return only the even rows (when sorting the rows by brand's name in descending order) and also return the row number (when sorted by brand in descending order).

WITH CTE AS (
    SELECT 
        F.BRAND AS brand, 
        F.SUGAR / 243 AS choc_num, 
        ROUND(AVG(CAST(B.CHOCOLATES AS FLOAT)), 2) AS choc_avg,
        ROW_NUMBER() OVER (ORDER BY F.BRAND DESC) AS row_num
    FROM 
        FACTORY AS F 
    INNER JOIN 
        BOOK AS B 
    ON 
        F.BRAND = B.BRAND
    GROUP BY 
        F.BRAND, F.SUGAR
)

SELECT 
    BRAND, 
    choc_num, 
    choc_avg, 
    row_num 
FROM 
    CTE
WHERE 
    row_num % 2 = 0
ORDER BY 
    choc_avg DESC;
