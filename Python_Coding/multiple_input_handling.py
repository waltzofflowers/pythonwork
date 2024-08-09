a, b = map(int, input().split())

average_list = []
total_list = []

for _ in range(b):
    place_holder = list (map (float, input().split()))
    total_list.append(place_holder)

for i in range(a):
    total = 0
    for j in range(b):
        total = total + total_list[j][i]
    average = total / b
    average_list.append(average)

for i in average_list:
    print(i)


#Sample Input
#5 3
#89 90 78 93 88
#90 91 85 88 86
#91 92 83 89 90.5

#Sample Output
#90.0
#91.8
#82.0
#98.0
#85.5