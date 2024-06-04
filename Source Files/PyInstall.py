import os
os.system("pip install wget")
import wget
StartPath = os.getcwd()
os.chdir("C:\\")
os.mkdir("py")
os.chdir("C:\\py\\")
wget.download("https://raw.githubusercontent.com/009401Howes/HWSPyApp/main/Source%20Files/PySimpleGUI.py", "PySimpleGUI.py")
wget.download("https://raw.githubusercontent.com/009401Howes/HWSPyApp/main/Source%20Files/py.py", "py.py")
os.chdir(StartPath)
wget.download("https://raw.githubusercontent.com/009401Howes/HWSPyApp/main/Source%20Files/PyStart.py", "PyStart.py")
exit
