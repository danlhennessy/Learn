#print(dir(int))

string = "Hello i am here"

string1 = ""
for v in string:
    if v == " ":
        string1 += "-"
    else:
        string1 += v
print(string1)