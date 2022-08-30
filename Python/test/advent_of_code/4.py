import pandas as pd
import numpy as np

my_input = [76,69,38,62,33,48,81,2,64,21,80,90,29,99,37,15,93,46,75,0,89,56,58,40,92,47,8,6,54,96,12,66,83,4,70,19,17,5,50,52,45,51,18,27,49,71,28,86,74,77,11,20,84,72,23,31,16,78,91,65,87,79,73,94,24,68,63,9,88,82,30,42,60,13,67,85,44,59,7,53,22,1,26,41,61,55,43,39,3,35,25,34,57,10,14,32,97,95,36,98]
    
df = pd.read_excel('D:/Backup/Work/DevOps/Programming/Learn/Python/test/advent_of_code/4.xlsx')
    
test_arr = df['boards'].to_numpy()
new_arr = np.array_split(test_arr, 100)


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

all_horizontal = horizontal_all(new_arr)

def vertical_all(multi_arr):
    arguments = []
    temp = np.transpose(multi_arr)
    for v in temp:
        split = np.array_split(v, 100)
        arguments.append(split)
    return np.concatenate(arguments, axis=0)

all_vert = vertical_all(all_horizontal)

horiz = all_horizontal.tolist()

horiz_vert = all_horizontal.tolist() + all_vert.tolist()



def check(numlist):
    for num in numlist:
        for index, block in enumerate(horiz_vert):
            if str(num) in block:
                block.remove(str(num))
                if block == []:
                    return(index, num)


block_index, trigger_num = check(my_input)
print(block_index, trigger_num)  # Prints index of block where bingo is found and the number that triggers bingo

# When checking horizontal blocks, no.347 was the no. with the first bingo, with vertical blocks, the first bingo was triggered by a later number

print(all_horizontal[346])
winning_block = horiz[345:350]  # Bingo 5x5 grid every 5 rows so 345:350 = winning grid
print(winning_block)

for num in my_input[:34]:  # numbers up to the index of the first number to trigger bingo (4)
    for row in winning_block:
        if str(num) in row:
            row.remove(str(num))
res = 0
for row in winning_block:
    for item in row:
        res += int(item)
print(winning_block)
print(f"Final Score: {res * trigger_num}")