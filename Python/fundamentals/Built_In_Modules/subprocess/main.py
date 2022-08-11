import subprocess

# subprocess.Popen("C:\Program Files\Google\Chrome\Application\chrome.exe")

subprocess.call(['pwsh', '/c', 'ls'])  # pwsh.exe, run, ls

randnumber_process = subprocess.run(["python", "example.py"], capture_output=True)

print(randnumber_process.stdout)

magic_number_process = subprocess.run(["python", "magic_number.py"], capture_output=True)

print(magic_number_process.stdout)