import subprocess

# subprocess.Popen("C:\Program Files\Google\Chrome\Application\chrome.exe")

subprocess.call(['pwsh', '/c', 'ls'])  # pwsh.exe, run, ls

randnumber_process = subprocess.run(["python", r"Python\fundamentals\Built_In_Modules\subprocess\example.py"], capture_output=True)

print(randnumber_process.stdout)