#Open file and make it readable
employee_file = open("fundamentals\File Operations\employees.txt", "r")

#print(employee_file.read())

print(employee_file.readlines())

employee_file.close
