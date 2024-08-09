def triangle_check(a):
    b = int(a[0])
    c = int(a[1])
    d = int(a[2])

    if b + c >= d and c + d >= b and b + d >= c:
        return "YES"
    else:
        return "NO"

a = input()
a = a.replace(" ", "")

print(triangle_check(a))