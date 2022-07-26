
mylist = []


def loops(n):
    if n in mylist:
        print('Test')
    elif n == 1:
        return 'Test2'
    elif n not in mylist and n != 1:
        mylist.append(n)
        x = str(n)
        n = 0
        for v in x:
            n += (int(v) * int(v))
        loops(n)

loops(19)