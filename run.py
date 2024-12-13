from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import os
import psutil

PROCNAME = "obs64.exe"
USER_DATA_PATH = "C:\\Users\\Tanma\\AppData\\Local\\Google\\Chrome\\User Data"
OBS_PATH = "C:\\Program Files\\obs-studio\\bin\\64bit\\obs64.exe"

options = Options()
options.add_argument("--app=https://meet.google.com"); 
options.add_argument(f"user-data-dir={USER_DATA_PATH}")
options.add_argument("profile-directory=Default") 
driver = webdriver.Chrome(options=options)

for proc in psutil.process_iter():
    if proc.name() == PROCNAME:
        os.system("obs-cli recording start")
        break
else:
    print("OBS not found")
    os.system("cd C:\\Program Files\\obs-studio\\bin\\64bit && start obs64.exe  --startrecording --minimize-to-tray")


driver.get("https://meet.google.com")
print("RECORDING STARTED")
while True:
    try:
        _ = driver.window_handles
    except:
        break
    time.sleep(5)
r=os.system("obs-cli recording stop")
print("RECORDING DONE" ,r)
os.system(r'explorer.exe "C:\Users\Tanma\Videos"')
driver.quit()
