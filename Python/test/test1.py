a = "Helloort"
s = "aababcabc"



def goodsubs(s):
    t, k = 0, 3
    good = 0
    while k < len(s) + 1:
        myset = list(set(s[t:k]))
        print(myset)
        if len(myset) < 3:
            t += 1
            k += 1
        else:
            good += 1
            t += 1
            k += 1
    print(good)

goodsubs(s)