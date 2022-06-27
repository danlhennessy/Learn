#Write a function named add_dots that takes a string and adds "." in between each letter.

#Then, below the add_dots function, write another function named remove_dots that removes all dots from a string

def add_dots(string):
    dotstring = ""
    for i in range(len(string)):
        if i < (len(string)) -1:
            dotstring += string[i] + "."
        else:
            dotstring += string[i]
    print(dotstring)

add_dots("Hello")

def remove_dots(string):
    nodotstring = string.replace(".", "")
    print(nodotstring)

remove_dots("l.o.p.l.e")