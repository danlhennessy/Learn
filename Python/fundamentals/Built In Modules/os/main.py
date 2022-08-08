import os

os.chdir('C:/Users/danh1')
print(os.getcwd())  # Current Working Directory
print(os.listdir())  # ls

# os.mkdir('afolder')  # Make Directory
# os.rmdir('afolder')  # Remove
# os.rename('example.txt', 'newexample.txt')

for dirpath, dirnames, filenames in os.walk('D:/Backup/Work/DevOps/Programming/Scripts/Python/fundamentals/Built In Modules'):
    print('Current Path: ', dirpath)
    print ('Directories:', dirnames)
    print('Files: ', filenames)
    print()
    
os.system("notepad.exe")
