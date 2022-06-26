#Define a function named double_letters that takes a single parameter. The parameter is a string. 
#Your function must return True if there are two identical letters in a row in the string, and False otherwise.

def double_letters(string):
    prevletter = ""
    doubles = False
    for v in string:
        if v == prevletter:
            doubles = True
        else:
            prevletter = v
    return(doubles)

print(double_letters("Hongg"))