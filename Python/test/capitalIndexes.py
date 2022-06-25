#Capital indexes
#Write a function named capital_indexes. The function takes a single parameter, which is a string. Your function should return a list of all the indexes in the string that have capital letters.

def capital_indexes(string):
    mylist = []
    for i, v in enumerate(string):
        if v.isupper():
            mylist.append(i)
    return mylist        
print(capital_indexes("HeLlO"))