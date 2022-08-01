# Collections module - provides alternative data types: Counter, namedtuple, defaultdict, deque
from collections import Counter, namedtuple, defaultdict, deque

a = "aaabbbccccc"
mycounter = Counter(a)  # Creates a dict with a count of each item in string a
print(mycounter)
print(mycounter.most_common(1))  # Prints most common single item in mycounter with counts
print(list(mycounter.elements()))  # Turns counter object into iterable

Point = namedtuple('Vector', 'x,y')  # Vector = name of tuple and shows when printing object
pt = Point(1, -4)
print(pt, pt.x, pt.y)

d = defaultdict(int)
d['a'] = 1
d['b'] = 2
print(d['c'])  # If key does not exist, it will return the default value of the data type provided. e.g. for int, default = 0, for float, default = 0.0

deq = deque()  # Double sided queue, can interact with both sides
deq.append(1)
deq.appendleft(26)
deq.extendleft([4,5,77])
deq.popleft()
print(deq)
deq.rotate(3)  # Shift all items to the right by 3 index places
print(deq)