from collections import deque, namedtuple

myqueue = deque([1,2,3,4,5,5])

cap_city = namedtuple('capital', ['country', 'city'])

myqueue.appendleft(21)
myqueue.append(21)

mytup = cap_city('Germany', 'Berlin')

print(myqueue, mytup)

mylist = [1,2,3,4,5,7,7,7,7,7,7]

a, b, *rest = mylist
print(rest)

print('new test')