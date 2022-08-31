from collections import namedtuple
import re

with open('D:/Backup/Work/DevOps/Programming/Learn/Python/test/advent_of_code/5.txt')  as f:
    my_input = f.readlines()

point = namedtuple('point', ['x', 'y'])

x_list = []
y_list = []
points_list = []

for line in my_input:
    x1, y1, x2, y2 = re.findall(r'\d+', line)
    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
    if x1 == x2 and y1 == y2:
        x_list.append(x1)
        y_list.append(y1)
        points_list.append(point(x1, y1))
    if x1 == x2 and y1 != y2:
        x_list.append(x1)
        y_list += list(range(min(y1, y2), max(y1, y2)))
        for v in list(range(min(y1, y2), max(y1, y2))):
            points_list.append(point(x1, v))
    if x1 != x2 and y1 == y2:
        y_list.append(y1)
        x_list += list(range(min(x1, x2), max(x1, x2)))
        for v in list(range(min(x1, x2), max(x1, x2))):
            points_list.append(point(v, y1))
        
# Ignoring cases where x1 != x2 and y1 != 2 for now


print(points_list[0])

if (517, 570) in points_list:
    print("helloo")
