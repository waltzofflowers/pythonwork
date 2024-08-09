if __name__ == '__main__':
    list1 = []
    a = []
    N = int(input())
    for _ in range (N):
        a = input().split()
        if a[0] == "insert":
            list1.insert(int (a[1]), int (a[2]))
        elif a[0] == "remove":
            listl.remove(int(a[1]))
        elif a[0] == "append":
            listl.append(int (a[1]))
        elif a[0] == "print":
            print(list1)
        elif a[0] == "sort":
            listl.sort()
        elif a[0] == "pop":
            list1.pop()
        elif a[0] == "reverse":
            list1.reverse()

#Multiple input lines dealing with list