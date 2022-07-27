def isiso(s, t):
    mydicts = {}
    mydictt = {}
    anslists = []
    anslistt = []
    for v in s:
        if v not in mydicts:
            mydicts[v] = 1
            anslists.append(mydicts[v])
        else:
            mydicts[v] += 1
            anslists.append(mydicts[v])
    for v in t:
        if v not in mydictt:
            mydictt[v] = 1
            anslistt.append(mydictt[v])
        else:
            mydictt[v] += 1
            anslistt.append(mydictt[v])
    print(anslists, anslistt)
    print(mydicts, mydictt)
    if anslists == anslistt:
        return True
    else:
        return False

print(isiso('bbbaaaba', 'aaabbbba'))