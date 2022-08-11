from pathlib import Path # Pathlib - Working with file paths

p = Path('.')  # Creates a path object in found OS (Windows Path)

test = [x for x in p.iterdir() if x.is_dir()]
print(p.resolve())  # Show file dir in your OS format (D:\Backup\Work\DevOps\Programming\Scripts\Python\fundamentals\Built In Modules\pathlib)
new_p = p / 'Test dir'  # Navigating into Test dir folder
new_p.mkdir()  # Create folder at location p
for file_name in new_p.iterdir():
    if file_name.match('*.txt') or file_name.match('*.py'):  # Check for specific file types when iterating through files in path
        print(file_name)

new_p /= 'test.txt'
print(new_p)
with new_p.open() as f:
    print(f.readline())
    print(f.readline())
