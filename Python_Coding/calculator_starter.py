#from replit import clear

def add(a, b):
  return a + b

def subtract(a, b):
  return a - b

def multiply(a, b):
  return a * b

def divide(a, b):
  return a / b


first_number = float(input("What's the first number?: "))

print("+\n-\n*\n/\n")

total = 0

while True:

  operand = input("Pick an operation: ")

  second_number = float(input("What's the next number?: "))

  operations = {"+": add,
                "-": subtract,
                "*": multiply,
                "/": divide
                }

  operation_hold = operations[operand]

  total = operation_hold(first_number, second_number)

  continue_calculation = input(f"Type 'y' to continue calculating with {total}, or type 'n' to start new calculation\n")

  if continue_calculation == "y":
    first_number = total

  elif continue_calculation == "n":
    #clear()
    first_number = float(input("What's the first number?: "))
    print("+\n-\n*\n/\n")