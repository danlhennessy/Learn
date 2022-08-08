#Open file and make it readable
employee_file = open("fundamentals/File Operations/employees.txt", "r")

#print(employee_file.read())

print(employee_file.readlines())

employee_file.close

# Content manager: Auto closes when finished. Preferred method
with open('fundamentals/File Operations/employees.txt', 'r') as f:
    f_contents = f.read(14)  # Can use an int as an argument to limit characters read from file
    print(f_contents)
    f_contents = f.read(15) 
    print(f_contents)
    f.seek(0)  # Navigate back to index 0 char in file
    f_contents = f.read(10)
    print(f_contents)
    
with open('fundamentals/File Operations/test.txt', 'w') as f:
    f.write('Hello WOrld, ')
    f.write('Continue where left off')