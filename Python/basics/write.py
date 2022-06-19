#Open file and make it appendable
#employee_file = open("basics/employees.txt", "a")

#Open file and make it appendable
employee_file = open("basics/employees.txt", "w")

#employee_file.write("Toby - Human Resources")

#\n forces entry to be on a new line
employee_file.write("\nKelly - Customer Service")

employee_file.close