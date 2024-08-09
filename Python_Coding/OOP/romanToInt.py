class Solution(object):
    def romanToInt(self, s):
        total = 0

        dict1 = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        dict2 = {"IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}
        
        for i in dict2:
            if i in s:
                total = total + int(dict2[i])
                s = s.replace(i, '')

        for j in s:
            if j in dict1:
                total = total + int(dict1[j])
        return total


sol = Solution()

s = "LVIII"

print(sol.romanToInt(s))
