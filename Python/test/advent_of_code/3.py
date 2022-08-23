


with open('D:/Backup/Work/DevOps/Programming/Learn/Python/test/advent_of_code/3.txt') as f:
    mylist = f.readlines()
    decimals = [int(bin, 2) for bin in mylist]
    
print(decimals)