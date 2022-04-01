num1 = float(input("Enter first number: "))
op = input("Enter operator: ")
num3 = float(input("Enter second number: "))

if op == "+":
    print(num1 + num3)
elif op == "-":
    print(num1 - num3)
elif op == "/":
    print(num1 / num3)
elif op == "*":
    print(num1 * num3)
else:
    print("Invalid LOperators")
