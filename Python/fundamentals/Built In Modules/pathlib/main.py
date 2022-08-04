from pathlib import Path # Pathlib - operations on file system paths

p = Path('.')
test = [x for x in p.iterdir() if x.is_dir()]
print(test)
test2 = list(p.glob('**/*.py'))
a,*rest = test2
print(test2)
print(a)