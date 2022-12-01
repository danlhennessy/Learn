with open('D:/Backup/Work/DevOps/Programming/Learn/Python/test/advent_of_code2022/1/1.txt') as f:
    test = f.readlines()

biglist = []
rollinglist = []

for item in test:
    if item != '\n':
        rollinglist.append(int(item.replace("\n", "")))
    else:
        biglist.append(rollinglist)
        rollinglist = []
biglist.append(rollinglist)

print(sum(max(biglist, key = sum)))