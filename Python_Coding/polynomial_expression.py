def polynomial(polynomial_exp, x):
    result = eval(polynomial_exp)
    return result

x, y = map(int, input().split())

polynomial_exp = input()

resultt = polynomial(polynomial_exp, x)

if resultt == y:
    print("True")
else:
    print("False")


#Sample input
#1 4    İnput 1
#x**3 + x**2 + x + 1   İnput 2

#Sample output
# True or False