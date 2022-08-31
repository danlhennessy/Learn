from collections import namedtuple
import matplotlib.pyplot as plt
import re
import numpy as np

with open('D:/Backup/Work/DevOps/Programming/Learn/Python/test/advent_of_code/5.txt')  as f:
    my_input = f.readlines()

x_list = []
y_list = []

for line in my_input:
    x1, y1, x2, y2 = re.findall(r'\d+', line)
    if x1 == x2 and y1 == y2:
        x_list.append(int(x1))
        y_list.append(int(y1))
    if x1 == x2 and y1 != y2:
        x_list.append(int(x1))
        y_list += list(range(min(y1, y2), max(y1, y2)))
    if x1 != x2 and y1 == y2:
        y_list.append(int(y1))
        x_list += list(range(min(x1, x2), max(x1, x2)))
        
# Ignoring cases where x1 != x2 and y1 != 2 for now

for i in range(0, len(x_list), 2):
    plt.plot(x_list[i:i+2], y_list[i:i+2], 'ro-')
    
# plt.show()

print(x_list)
