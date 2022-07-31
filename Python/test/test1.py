
password = "wbiRerewnurb222iewr"
def threerepeat(passw):
    ans = True
    mydict = {}
    for v in passw:
        if v not in mydict:
            mydict = {}
            mydict[v] = 1
        else:
            mydict[v] += 1
            if mydict[v] == 3:
                print('3 in a row')
                ans = False
    return ans

if any(v.isupper() for v in password) and any(v.islower() for v in password) and any(v.isdigit() for v in password) and len(password) > 6 and len(password) < 21 and threerepeat(password) is not False:
    print("Yes")
    
