
num1 = float(input("Enter first number: "))
oper = (input("Enter operator: "))
num2 = float(input("Enter third number: "))

if oper == "+":
    print(num1 + num2)
elif oper == "-":
    print(num1 - num2)
elif oper == "/":
    print(num1 / num2)
elif oper == "*":
    print(num1 * num2)
else:
    print("Invalid operator")
