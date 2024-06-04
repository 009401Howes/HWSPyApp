import os
if os.path.isfile("PyInstall.py") == True:
	os.remove("PyInstall.py")
    print("Install file removed")
os.chdir("C:\\Py\\")
os.system("python py.py")
