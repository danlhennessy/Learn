import pandas as pd
import numpy as np
import numpy.ma as ma

my_input = [76,69,38,62,33,48,81,2,64,21,80,90,29,99,37,15,93,46,75,0,89,56,58,40,92,47,8,6,54,96,12,66,83,4,70,19,17,5,50,52,45,51,18,27,49,71,28,86,74,77,11,20,84,72,23,31,16,78,91,65,87,79,73,94,24,68,63,9,88,82,30,42,60,13,67,85,44,59,7,53,22,1,26,41,61,55,43,39,3,35,25,34,57,10,14,32,97,95,36,98]
    
df = pd.read_excel('D:/Backup/Work/DevOps/Programming/Learn/Python/test/advent_of_code/4.xlsx')
    
test_arr = df['boards'].to_numpy()
new_arr = np.array_split(test_arr, 100)  # Separate ndarray into grids of 5x5


def horizontal(arr):
    horiz_list = []
    for v in arr:
        split = v.split(' ')
        horiz_list.append(list(filter(None, split)))
    return np.array(horiz_list)


def vertical(arr):
    return np.transpose(horizontal(arr))


def horizontal_all(multi_arr):
    arguments = []
    for v in multi_arr:
        arguments.append(horizontal(v))
    return np.concatenate(arguments, axis=0)

all_horizontal = np.array_split(horizontal_all(new_arr), 100)  # formats elements correctly into strings and reorganises back into 5x5 grid

def mask_array(ndarray, num):
    return ma.masked_where(ndarray == str(num), ndarray)
    
for num in my_input[:20]:  # Masks elements from original input one by one
    all_horizontal = mask_array(all_horizontal, num)
    
print(ma.MaskedArray(all_horizontal))


# final = (check(my_input)) - 1  # Index of final block to get bingo, 475 in my case

winning_block = horiz[475:480]
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