import pandas as pd
import numpy as np
import numpy.ma as ma

my_input = [76,69,38,62,33,48,81,2,64,21,80,90,29,99,37,15,93,46,75,0,89,56,58,40,92,47,8,6,54,96,12,66,83,4,70,19,17,5,50,52,45,51,18,27,49,71,28,86,74,77,11,20,84,72,23,31,16,78,91,65,87,79,73,94,24,68,63,9,88,82,30,42,60,13,67,85,44,59,7,53,22,1,26,41,61,55,43,39,3,35,25,34,57,10,14,32,97,95,36,98]
    
df = pd.read_excel('D:/Backup/Work/DevOps/Programming/Learn/Python/test/advent_of_code/4.xlsx')
    
original_arr = df['boards'].to_numpy()
grid_arr = np.array_split(original_arr, 100)  # Separate ndarray into grids of 5x5


def horizontal(arr):
    horiz_list = []
    for v in arr:
        split = v.split(' ')
        horiz_list.append(list(filter(None, split)))
    return np.array(horiz_list)


def horizontal_all(multi_arr):
    arguments = []
    for v in multi_arr:
        arguments.append(horizontal(v))
    return np.concatenate(arguments, axis=0)

all_horizontal = np.array_split(horizontal_all(grid_arr), 100)  # formats elements correctly into strings, removes whitespace and reorganises back into 5x5 grid


def mask_array(ndarray, num):
    return ma.masked_where(ndarray == str(num), ndarray)

bingo_list = []
count = len(bingo_list)

for num in my_input:  # Masks elements from original input one by one
    all_horizontal = mask_array(all_horizontal, num)
    for i, v in enumerate(all_horizontal):
        horiz_count = ma.count_masked(v, axis=1)
        vert_count = ma.count_masked(v, axis=0)
        if 5 in horiz_count or 5 in vert_count:
            if i not in bingo_list:
                bingo_list.append(i)
    if len(bingo_list) == 100:
        print("last board done")
    print(num, bingo_list)


# print(winning_block)

# for num in my_input:
#     for row in winning_block:
#         if str(num) in row:
#             row.remove(str(num))
# res = 0
# for row in winning_block:
#     for item in row:
#         res += int(item)
#         print(res)
# print(winning_block)
# print(res * 98)