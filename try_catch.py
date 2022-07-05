
try:
#    value = 10/0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as err1:
    print(err1)

except ValueError as err2:
    print(err2)