#Open file and make it readable
employee_file = open("fundamentals\File Operations\employees.txt", "r")

#print(employee_file.read())

print(employee_file.readlines())

employee_file.close

# Content manager: Auto closes when finished. Preferred method
with open('fundamentals\File Operations\employees.txt', 'r') as f:
    f_contents = f.read(100)  # Can use an int as an argument to limit characters read from file
    print(f_contents)