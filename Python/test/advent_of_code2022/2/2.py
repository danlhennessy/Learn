with open('D:/Backup/Work/DevOps/Programming/Learn/Python/test/advent_of_code2022/2/2.txt') as f:
    strategy = f.readlines()
    
print(strategy)

def total_score(strat: list):
    result = 0
    for line in strat:
        if line[2] == 'X' and line[0] == 'C':
            result += 7
        elif line[2] == 'X' and line[0] == 'A':
            result += 4
        elif line[2] == 'X' and line[0] == 'B':
            result += 1
        elif line[2] == 'Y' and line[0] == 'A':
            result += 8
        elif line[2] == 'Y' and line[0] == 'B':
            result += 5
        elif line[2] == 'Y' and line[0] == 'C':
            result += 2
        elif line[2] == 'Z' and line[0] == 'B':
            result += 9
        elif line[2] == 'Z' and line[0] == 'C':
            result += 6
        elif line[2] == 'Z' and line[0] == 'A':
            result += 3
    return result

print(total_score(strategy))