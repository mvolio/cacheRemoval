import os
import shutil
import time
import subprocess
import glob
import fnmatch

os.system('taskkill /f /im chrome.exe')
os.system('taskkill /f /im iexplore.exe')
os.system('taskkill /f /im firefox.exe')
time.sleep(2)
user = os.getlogin()

os.chdir("C:/Users/%s/AppData/Local/Mozilla/Firefox/Profiles/" % user)

for file in os.listdir("C:/Users/%s/AppData/Local/Mozilla/Firefox/Profiles/" % user):
    if fnmatch.fnmatch(file, "*.default*"):
        firefoxProfile = file

dict = {'chromeL': "C:/Users/%s/AppData/Local/Google/Chrome/User Data/Default/Cache" % user,
 'firefoxL': "C:/Users/%s/AppData/Local/Mozilla/Firefox/Profiles/%s/cache2" % (user, firefoxProfile),
  'internetexplorerL': "C:/Users/%s/AppData/Local/Microsoft/Windows/INetCache/Low/IE" % user}
  #internetexplorerSeven = "C:/Users/%s/AppData/Local/Microsoft/Windows/Temporary" % user

path = "C:/Users/%s/AppData/Local/Google/Chrome/User Data" % user

os.chdir("C:/Users/%s/AppData/Local/Google/Chrome/User Data/Default" % user)

try:
    shutil.rmtree(dict["chromeL"])
    print("Chrome cache deleted")
except OSError as err:
    print("Chrome cache does not exist")
try:
    shutil.rmtree(dict["firefoxL"])
    print("Firefox cache deleted")
except OSError as err:
    print("Firefox cache file does not exist")
try:
    shutil.rmtree(dict["internetexplorerL"])
    print("IE cache deleted")
except OSError as err:
    print("Internet Explorer cache file does not exist")

#for loop for trying the firefox dictionary items
#os.mkdir("C:/Users/%s/AppData/Local/Google/Chrome/User Data/Default/Cache" % user)

app = 'chrome.exe'
appPath = os.path.join('C:/Program Files (x86)/Google/Chrome/Application', app)

subprocess.Popen(app, executable=appPath)
