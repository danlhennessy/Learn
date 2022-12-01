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

top3 = 0
x = 0
while x < 3:
    currentmax = (max(biglist, key = sum))
    print(sum(max(biglist, key = sum)))
    top3 += (sum(max(biglist, key = sum)))
    biglist.remove(currentmax)
    x += 1
    
print(top3)