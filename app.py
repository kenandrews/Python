
employee_file = open("employee.txt", "r")
#print(employee_file.read())
#print(employee_file.readline())
#print(employee_file.readlines())
print(employee_file.readlines()[2])

employee_file.close()
