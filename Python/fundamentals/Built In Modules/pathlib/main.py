from pathlib import Path # Pathlib - Working with file paths

p = Path('.')  # Creates a path object in found OS (Windows Path)

test = [x for x in p.iterdir() if x.is_dir()]
print(p.resolve())  # Show file dir in your OS format (D:\Backup\Work\DevOps\Programming\Scripts\Python\fundamentals\Built In Modules\pathlib)
new_p = p / 'Test dir'
new_p.mkdir()  # Create folder at location p