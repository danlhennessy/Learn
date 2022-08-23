import pandas as pd

df = pd.read_excel('D:/Backup/Work/DevOps/Programming/Learn/Python/test/advent_of_code/1.xlsx')

prev = df.iloc[0]['depth']
count = 0
for index, row in df.iterrows():
    if row['depth'] > prev:
        count += 1
    prev = row['depth']
    
print(count)