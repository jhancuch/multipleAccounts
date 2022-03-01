import subprocess

#completed = subprocess.run(["powershell", "choco"], capture_output=True)
#completed = subprocess.run([r'C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe', r'choco'], capture_output=True)

try:
    chocoCheck = subprocess.check_output([r"C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe", r"choco"], shell=True) 
except:
    task1 = subprocess.run([r"C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe", r"Set-ExecutionPolicy Bypass -Scope Process -Force; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))"], capture_output=True)
    print(task1)
