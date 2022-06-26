#Write a function named mid that takes a string as its parameter. Your function should extract and return the middle letter. 
#If there is no middle letter, your function should return the empty string.

def mid(string):
    if len(string) % 2 == 0:
        return ""
    elif True:
        rollingsum = 0
        for i in string:
            if rollingsum + 1 > (len(string) / 2):
                return i
            else:
                rollingsum += 1
            
print(mid("ac"))