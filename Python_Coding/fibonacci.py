def k(i):
    total = [0, 1]
    for i in range(2, i + 1):
        total.append(total[i - 1] + total[i - 2])

    print(total[i])

i = 7

k(i)