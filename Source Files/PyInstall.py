import os
os.system("pip install wget")
import wget
StartPath = os.getcwd()
os.chdir("C:\\")
os.mkdir("py")
os.chdir("C:\\py\\")
wget.download("https://publicassets.w3spaces.com/PySimpleGUI.html", "PySimpleGUI.py")
wget.download("https://publicassets.w3spaces.com/py.html", "py.py")
os.chdir(StartPath)
wget.download("https://publicassets.w3spaces.com/PyStart.html", "PyStart.py")
exit
