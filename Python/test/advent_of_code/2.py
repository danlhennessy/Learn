import pandas as pd

df = pd.read_excel('D:/Backup/Work/DevOps/Programming/Learn/Python/test/advent_of_code/2.xlsx')


df['steps'] = df['moves'].str.strip().str[-1]
df['direction'] = df['moves'].str.strip().str[0]
df["steps"] = df["steps"].astype(int)
df.loc[df['direction'].str.contains("u"), "steps"] *= -1

horizontal_steps = df[df['direction'] == 'f'].drop(columns=['moves', 'direction'])
depth_steps = df[df['direction'] != 'f'].drop(columns=['moves', 'direction'])

print(depth_steps.sum() * horizontal_steps.sum())