import os
os.system("pip install wget")
from fileinput import filename
from typing import Text
import time
DebugMode = True
import wget
import shutil
FileWorkingDirectory = os.getcwd()
WindowRenderExist = os.path.isfile("PySimpleGUI.py")
UserFolderExist = os.path.isdir("Users")
if UserFolderExist == False:
    os.mkdir("Users")
if WindowRenderExist == False:
    URL = "https://publicassets.w3spaces.com/PySimpleGUI.html"
    response = wget.download(URL, "PySimpleGUI.py")
import PySimpleGUI as sg
DebugMode = os.path.isfile("Debug.txt")
Is_Set_Up = os.path.exists("Temp.txt")
UsersWorkingDirectory = os.getcwd() + "//Users//"
while Is_Set_Up == False:
    AdminPassword = sg.popup_get_text("First time setting up. Enter admin password")
    if AdminPassword == "":
        sg.popup_annoying("Please enter a password for admin.")
    else:
        TempFileOpen = open("Temp.txt", "w")
        TempFileOpen.write(AdminPassword)
        TempFileOpen.close()
        Is_Set_Up = True
        break      
def LoginSystem():
    #setting up layout
    global Username, UserPath
    Username = ""
    layout = [
        [sg.Text("Username"), sg.Input(key="UsernameInput", expand_x=True)],
        [sg.Text("Password"), sg.Input(key="PasswordInput", password_char="·", expand_x=True)],
        [sg.Button("login"), sg.Button("register"), sg.Button("Exit")]]
    #Building Window
    LoginWindow = sg.Window('login', layout, size=(300,100))
    def AdminMode():
        LoginWindow.disappear()
        LoginWindow.disable()
        Admin_Window_Layout = [
            [sg.Button("View Users"), sg.Button("Edit User's password"), sg.Button("Edit Admin Password")], [sg.Button("Delete User"), sg.Button("Debug Mode"), sg.Button("Exit")]
        ]
        Admin_Window = sg.Window("Administrator Mode", Admin_Window_Layout, size=(600,200))
        Admin_Window_Open = True
        while Admin_Window_Open == True:
            Admin_events, Admin_Values = Admin_Window.read()
            if Admin_events=="Exit" or Admin_events == sg.WIN_CLOSED:
                LoginWindow.enable()
                LoginWindow.reappear()
                Admin_Window.close()
                Admin_Window_Open = False
                
            elif Admin_events=="View Users":
                os.chdir(UsersWorkingDirectory)
                l=os.listdir()
                li=[x.split('.')[0] for x in l]
                sg.popup_annoying(li)
                os.chdir(FileWorkingDirectory)
            elif Admin_events=="Edit User's password":
                os.chdir(UsersWorkingDirectory)
                User = sg.popup_get_text("What user(no '.txt')") + ".txt"
                Does_User_Exist = os.path.isfile(User)
                if Does_User_Exist == True:
                    UserFile = open(User, "w")
                    User_Password = sg.popup_get_text("Enter user password", password_char="*")
                    UserFile.write(User_Password)
                    UserFile.close()
                    os.chdir(FileWorkingDirectory)
            elif Admin_events=="Edit Admin Password":
                os.chdir(FileWorkingDirectory)
                AdminFile = open("Temp.txt", "w")
                Password = sg.popup_get_text("Enter new admin password")
                AdminFile.write(Password)
                AdminFile.close()
            elif Admin_events=="Delete User":
                os.chdir(UsersWorkingDirectory)
                UserToDelete = sg.popup_get_text("What user do you want to delete?")
                if UserToDelete == "Exit":
                    break
                UserToDeleteFile = UserToDelete + ".txt"
                Does_User_Exist = os.path.isfile(UserToDeleteFile)
                if Does_User_Exist == True:
                    os.remove(UserToDeleteFile)
                    shutil.rmtree(UserToDelete)
                os.chdir(FileWorkingDirectory)
            elif Admin_events == "Debug Mode":
                DebugFile = open("Debug.txt", "x")
                DebugMode.close()
        break
    global LoggedIn
    LoggedIn = False
    while LoggedIn == False:
        event, LoginValues = LoginWindow.read()
        if event == sg.WIN_CLOSED or event=="Exit":
            exit()
        if event == "login" and LoginValues["UsernameInput"] != "":
            if LoginValues["PasswordInput"] == "":
                sg.popup_ok("Please enter a password.")
                break
            os.chdir(UsersWorkingDirectory)
            Input_Username = LoginValues["UsernameInput"]
            Input_Username_File = LoginValues["UsernameInput"] + ".txt"
            Does_User_Exist = os.path.exists(Input_Username_File)
            if Does_User_Exist == True:
                User_File = open(Input_Username_File, "r")
                User_Password = User_File.read()
                User_File.close()
                if LoginValues["PasswordInput"] == User_Password:
                    Username = Input_Username
                    UserPath = UsersWorkingDirectory + Input_Username + "//"
                    os.chdir(UserPath)
                    LoggedIn = True
                    LoginWindow.disappear()
                    LoginWindow.close()
                else:
                    sg.popup_annoying("Password incorrect.")
                    os.chdir(FileWorkingDirectory)
            elif LoginValues["UsernameInput"] == "admin":
                os.chdir(FileWorkingDirectory)
                Admin_File = open("Temp.txt", "r")
                AdminPassword = Admin_File.read()
                if LoginValues["PasswordInput"] != AdminPassword:
                    sg.popup_annoying("Incorrect.")
                else:
                    AdminMode()
                    LoginValues{"UsernameInput] = None
                    LoginValues{"PasswordInput] = None
                    
            else:
                sg.popup_annoying("User doesn't exist.")
        elif event == "register":
            LoginWindow.disable()
            LoginWindow.disappear()
            loop = True
            loginLayout = [[sg.Text("Enter Username"), sg.Input(key="User_Register_Username")], [sg.Text("Enter Password"), sg.Input(key="User_Register_Password", password_char="*")], [sg.Button("register"), sg.Button("login"), sg.Button("Exit")]]
            RegisterWindow = sg.Window("Register", loginLayout, size=(300,100))
            while loop == True:
                events, value = RegisterWindow.read()
                if events == "Exit" or events == sg.WIN_CLOSED:
                    exit()
                elif events == "login":
                    LoginWindow.reappear()
                    LoginWindow.enable()
                    RegisterWindow.close()
                    event = "login"
                    loop = False

                elif events =="register":
                    if value["User_Register_Username"] == "" or value["User_Register_Password"] == "":
                        sg.popup_annoying("Username or password cannot be empty.")
                    else:
                        os.chdir(UsersWorkingDirectory)
                        User_File = value["User_Register_Username"] + ".txt"
                        Does_User_Exist = os.path.isfile(User_File)
                        if Does_User_Exist == True:
                            sg.popup_annoying("User already exists.\n")
                        elif value["User_Register_Username"] == "admin":
                            sg.popup_annoying("Unavailable.")
                        else:
                            os.mkdir(value["User_Register_Username"])
                            UserFile = open(User_File, "w")
                            User_Password = value["User_Register_Password"]
                            UserFile.write(User_Password)
                            UserFile.close()
                            UserDirectory = UsersWorkingDirectory + value["User_Register_Username"]
                            os.chdir(UserDirectory)
                            Username = value["User_Register_Username"]
                            LoggedIn = True
                            RegisterWindow.disappear()
                            RegisterWindow.close()
                            LoginWindow.close()
                            break
        else:
            sg.popup_annoying("Please enter a username.")
def TextEditor():
        Break = False
        textsave = ""
        fileName = ""
        StartWindow = True
        TextEditor_Start_Window_Layout = [
            [sg.Button("Edit File"), sg.Button("Create File"), sg.Button("Delete File")]
        ]
        TextEditor_Start_Window = sg.Window("Text Editor", TextEditor_Start_Window_Layout, size =(300,100))
        while StartWindow == True:
            TextEditor_Start_Window_event, TextEditor_Start_Window_Value = TextEditor_Start_Window.read()
            if TextEditor_Start_Window_event == sg.WIN_CLOSED or TextEditor_Start_Window_event == "Exit":
                TextEditor_Start_Window.close()
                StartWindow = False
                Break = True
            elif TextEditor_Start_Window_event == "Create File":
                FileName = sg.popup_get_text("Enter the file name")
                CreateFileCheck = os.path.isfile(FileName)
                if CreateFileCheck == True:
                    sg.popup_annoying("File already exists.")
                else:
                    FileCreate = open(FileName, "x")
                    fileName = FileName
                    break
            elif TextEditor_Start_Window_event == "Edit File":
                FileName = sg.popup_get_text("Enter the file name")
                input(os.getcwd())
                EditFileCheck = os.path.isfile(FileName)
                if EditFileCheck == True:
                    FileEdit = open(FileName, "a")
                    textsave = FileEdit.read()
                    FileEdit.close()
                    break
                else:
                    sg.popup_annoying("File doesn't exist.")    
            elif TextEditor_Start_Window_event == "Delete File":
                FileName = sg.popup_get_text("Enter the file name")
                DeleteFileCheck = os.path.isfile(FileName)
                if DeleteFileCheck == True:
                    os.remove(FileName)
                else:
                    sg.popup_annoying("File doesn't exist.")
        if Break == False:
           TextEditor_Layout= [
           [sg.Text("Input"), sg.Multiline(key="TextEditorInput", default_text = textsave, enable_events=True, expand_x=True, expand_y=True, justification='left')],
           [sg.Button("Save")]]
           TextEditor_Window = sg.Window("Text Editor", TextEditor_Layout, enable_close_attempted_event=True, size =(600,600))
           while True:
               TextEditor_Event, TextEditor_Values = TextEditor_Window.read()
               if TextEditor_Event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT or TextEditor_Event == "Exit":
                   CloseCheck = sg.popup_ok_cancel("Are you sure you want to quit?")
                   if CloseCheck == "OK":
                       TextEditor_Window.close()
                       break
               elif TextEditor_Event == "Save":
                   File = open(fileName, "w")
                   File.write(TextEditor_Values["TextEditorInput"])
                   File.close()
if DebugMode == False:
    LoginSystem()
LoggedIn = True
#Main Window
MainWindowlayout = [[sg.Button("Files"), sg.Button("Log Out"), sg.Button("Text Editor")], [sg.Button("Open"), sg.Button("Calculator"), sg.Button("Power")], [sg.Button("Exit")]]
MainWindow = sg.Window("App", MainWindowlayout, size=(1920,1080))
print ("Create Main Window")
while True:
    event, Values = MainWindow.read()
    if event == sg.WIN_CLOSED or event =="Exit":
        exit()
    elif event == "Log Out":
        Username = ""
        MainWindow.close()
        LoggedIn = False
        os.chdir(FileWorkingDirectory)
        LoginSystem()
    elif event == "Text Editor":
        TextEditor()
    elif event == "Open":
        sg.popup_annoying(os.listdir("C://ProgramData//Microsoft//Windows//Start Menu//Programs//"))
    elif event == "Calculator":
        os.chdir(FileWorkingDirectory)
        CalculatorFile = FileWorkingDirectory + "//Calculator.py"
        CalculatorFileExist = os.path.isfile(CalculatorFile)
        if CalculatorFileExist == False:
            URL = "https://raw.githubusercontent.com/009401Howes/HWSPyApp/main/Source%20Files/calcApp.py"
            response = wget.download(URL, "Calculator.py")
            try:
                import Calculator
                os.chdir(UserPath)
            except:
                sg.popup_annoying("Unable to download file.")
        else:
            os.chdir(FileWorkingDirectory)
            import Calculator
            os.chdir(UserPath)
    elif event == "Files":
        os.chdir(FileWorkingDirectory)
        ExplorerFileExist = os.path.isfile("Explorer.py")
        if ExplorerFileExist == False:
            URL ="https://raw.githubusercontent.com/009401Howes/HWSPyApp/main/Source%20Files/calcApp.py"
            response = wget.download(URL, "Explorer.py")
            try:
                import Explorer
                os.chdir(UserPath)
            except:
                sg.popup_annoying("Unable to download file.")
            else:
                os.chdir(FileWorkingDirectory)
                import Explorer
                os.chdir(UserPath)
    elif event == "Power":
        PowerWindowOpen = True
        PowerWindowLayout = [[sg.Button("Sleep"), sg.Button("Hibernate"), sg.Button("Shutdown"), sg.Button("Restart"), sg.Button("BIOS")]]
        PowerWindow  = sg.Window("Power Window", PowerWindowLayout, enable_close_attempted_event = True, size = (400, 50))
        while PowerWindowOpen == True:
            PowerWindow_Event, PowerWindow_Values = PowerWindow.read()
            if PowerWindow_Event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT or PowerWindow_Event == "Exit":
                   CloseCheck = sg.popup_ok_cancel("Are you sure you want to quit?")
                   if CloseCheck == "OK":
                       PowerWindow.close()
                       break
            elif PowerWindow_Event == "Sleep":
                os.system("psshutdown64.exe -d -t 0")
            elif PowerWindow_Event == "Hibernate":
                os.system("shutdown /h")
            elif PowerWindow_Event == "Shutdown":
                os.system("shutdown /s")
            elif PowerWindow_Event == "Restart":
                os.system("shutdown /r")
            elif PowerWindow_Event == "BIOS":
                AdminPass = ""
                os.chdir(FileWorkingDirectory)
                TempFileOpen = open("Temp.txt", "w")
                AdminPass = TempFileOpen.read()
                TempFileOpen.close()
                BIOSLock = sg.popup_get_text("Admin Password")
                if BIOSLock == AdminPass:
                    os.system("shutdown /r /fw")
                os.chdir(UserPath)
