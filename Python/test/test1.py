phoneNumber = "3662277"
words = ["foo", "bar", "baz", "foobar", "emo", "cap", "car", "cat"]

# Convert word in words to phone digit
# Iteration for checking substring

def convert(mylist):
    newlist = []
    for word in mylist:
        newword = word.replace('a', '2')
        newlist.append(newword)
    return(newlist)



def checknum(convlist):
    anslist = []
    convanslist = []
    for word in convlist:
        wordlist = list(word)
        if wordlist in list(phoneNumber):
            anslist.append(word)
    for word in anslist:
        newword = word.replace('2', 'a')
        convanslist.append(newword)
    print(convanslist)

checknum(convert(words))