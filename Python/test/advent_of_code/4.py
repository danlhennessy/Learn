import pandas as pd
import numpy as np

my_input = [76,69,38,62,33,48,81,2,64,21,80,90,29,99,37,15,93,46,75,0,89,56,58,40,92,47,8,6,54,96,12,66,83,4,70,19,17,5,50,52,45,51,18,27,49,71,28,86,74,77,11,20,84,72,23,31,16,78,91,65,87,79,73,94,24,68,63,9,88,82,30,42,60,13,67,85,44,59,7,53,22,1,26,41,61,55,43,39,3,35,25,34,57,10,14,32,97,95,36,98]
    
df = pd.read_excel('D:/Backup/Work/DevOps/Programming/Learn/Python/test/advent_of_code/4.xlsx')
    
test_arr = df['boards'].to_numpy()
new_arr = np.array_split(test_arr, 100)



def top(arr):
    split = arr[0].split(' ')
    return list(filter(None, split))


def right(arr):
    right_lst = []
    for v in arr:
        right_lst.append(v[-2:])
    return [x.strip(' ') for x in right_lst]

def bottom(arr):
    split = arr[4].split(' ')
    return list(filter(None, split))

def left(arr):
    left_lst = []
    for v in arr:
        left_lst.append(v[:2])
    return [x.strip(' ') for x in left_lst]

print(new_arr[1])

    
print(right(new_arr[1]))