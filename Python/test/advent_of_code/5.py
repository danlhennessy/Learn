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
    if x1 == x2 or y1 == y2:
        x_list.append(int(x1)), x_list.append(int(x2))
        y_list.append(int(y1)), y_list.append(int(y2))

for i in range(0, len(x_list), 2):
    plt.plot(x_list[i:i+2], y_list[i:i+2], 'ro-')
    
# plt.show()



bor, zor = x_list[0], x_list[1]

print(max(zor, bor), min(zor, bor))
