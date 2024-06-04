From: <Saved by Blink>
Snapshot-Content-Location: https://publicassets.w3spaces.com/py.html
Subject: 
Date: Tue, 4 Jun 2024 12:55:29 +0100
MIME-Version: 1.0
Content-Type: multipart/related;
	type="text/html";
	boundary="----MultipartBoundary--UCom1oT6dc4iPOvKj4Yjq9OQh2Gq4MKVRKp5fBlfOh----"


------MultipartBoundary--UCom1oT6dc4iPOvKj4Yjq9OQh2Gq4MKVRKp5fBlfOh----
Content-Type: text/html
Content-ID: <frame-8BE131F0E81A86BBC5A636AC42FDE4FA@mhtml.blink>
Content-Transfer-Encoding: quoted-printable
Content-Location: https://publicassets.w3spaces.com/py.html

<html><head><meta http-equiv=3D"Content-Type" content=3D"text/html; charset=
=3Dwindows-1252"></head><body>import os
os.system("pip install wget")
from fileinput import filename
from typing import Text
import time
DebugMode =3D True
import wget
import shutil
FileWorkingDirectory =3D os.getcwd()
WindowRenderExist =3D os.path.isfile("PySimpleGUI.py")
UserFolderExist =3D os.path.isdir("Users")
if UserFolderExist =3D=3D False:
    os.mkdir("Users")
if WindowRenderExist =3D=3D False:
    URL =3D "https://publicassets.w3spaces.com/PySimpleGUI.html"
    response =3D wget.download(URL, "PySimpleGUI.py")
import PySimpleGUI as sg
DebugMode =3D os.path.isfile("Debug.txt")
Is_Set_Up =3D os.path.exists("Temp.txt")
UsersWorkingDirectory =3D os.getcwd() + "//Users//"
while Is_Set_Up =3D=3D False:
    AdminPassword =3D sg.popup_get_text("First time setting up. Enter admin=
 password")
    if AdminPassword =3D=3D "":
        sg.popup_annoying("Please enter a password for admin.")
    else:
        TempFileOpen =3D open("Temp.txt", "w")
        TempFileOpen.write(AdminPassword)
        TempFileOpen.close()
        Is_Set_Up =3D True
        break     =20
def LoginSystem():
    #setting up layout
    global Username, UserPath
    Username =3D ""
    layout =3D [
        [sg.Text("Username"), sg.Input(key=3D"UsernameInput", expand_x=3DTr=
ue)],
        [sg.Text("Password"), sg.Input(key=3D"PasswordInput", password_char=
=3D"=C2=B7", expand_x=3DTrue)],
        [sg.Button("login"), sg.Button("register"), sg.Button("Exit")]]
    #Building Window
    LoginWindow =3D sg.Window('login', layout, size=3D(300,100))
    def AdminMode():
        LoginWindow.disappear()
        LoginWindow.disable()
        Admin_Window_Layout =3D [
            [sg.Button("View Users"), sg.Button("Edit User's password"), sg=
.Button("Edit Admin Password"), sg.Button("Delete User"), sg.Button("Debug =
Mode"), sg.Button("Exit")]
        ]
        Admin_Window =3D sg.Window("Administrator Mode", Admin_Window_Layou=
t, size=3D(600,200))
        Admin_Window_Open =3D True
        while Admin_Window_Open =3D=3D True:
            Admin_events, Admin_Values =3D Admin_Window.read()
            if Admin_events=3D=3D"Exit" or Admin_events =3D=3D sg.WIN_CLOSE=
D:
                LoginWindow.enable()
                LoginWindow.reappear()
                Admin_Window.close()
                Admin_Window_Open =3D False
            elif Admin_events=3D=3D"View Users":
                os.chdir(UsersWorkingDirectory)
                l=3Dos.listdir()
                li=3D[x.split('.')[0] for x in l]
                sg.popup_annoying(li)
                os.chdir(FileWorkingDirectory)
            elif Admin_events=3D=3D"Edit User's password":
                os.chdir(UsersWorkingDirectory)
                User =3D sg.popup_get_text("What user(no '.txt')") + ".txt"
                Does_User_Exist =3D os.path.isfile(User)
                if Does_User_Exist =3D=3D True:
                    UserFile =3D open(User, "w")
                    User_Password =3D sg.popup_get_text("Enter user passwor=
d", password_char=3D"*")
                    UserFile.write(User_Password)
                    UserFile.close()
                    os.chdir(FileWorkingDirectory)
            elif Admin_events=3D=3D"Edit Admin Password":
                os.chdir(FileWorkingDirectory)
                AdminFile =3D open("Temp.txt", "w")
                Password =3D sg.popup_get_text("Enter new admin password")
                AdminFile.write(Password)
                AdminFile.close()
            elif Admin_events=3D=3D"Delete User":
                os.chdir(UsersWorkingDirectory)
                UserToDelete =3D sg.popup_get_text("What user do you want t=
o delete?")
                if UserToDelete =3D=3D "Exit":
                    break
                UserToDeleteFile =3D UserToDelete + ".txt"
                Does_User_Exist =3D os.path.isfile(UserToDeleteFile)
                if Does_User_Exist =3D=3D True:
                    os.remove(UserToDeleteFile)
                    shutil.rmtree(UserToDelete)
                os.chdir(FileWorkingDirectory)
            elif Admin_events =3D=3D "Debug Mode":
                DebugFile =3D open("Debug.txt", "x")
                DebugMode.close()
    global LoggedIn
    LoggedIn =3D False
    while LoggedIn =3D=3D False:
        event, LoginValues =3D LoginWindow.read()
        if event =3D=3D sg.WIN_CLOSED or event=3D=3D"Exit":
            exit()
        if event =3D=3D "login" and LoginValues["UsernameInput"] !=3D "":
            if LoginValues["PasswordInput"] =3D=3D "":
                sg.popup_ok("Please enter a password.")
                break
            os.chdir(UsersWorkingDirectory)
            Input_Username =3D LoginValues["UsernameInput"]
            Input_Username_File =3D LoginValues["UsernameInput"] + ".txt"
            Does_User_Exist =3D os.path.exists(Input_Username_File)
            if Does_User_Exist =3D=3D True:
                User_File =3D open(Input_Username_File, "r")
                User_Password =3D User_File.read()
                User_File.close()
                if LoginValues["PasswordInput"] =3D=3D User_Password:
                    Username =3D Input_Username
                    UserPath =3D UsersWorkingDirectory + Input_Username + "=
//"
                    os.chdir(UserPath)
                    LoggedIn =3D True
                    LoginWindow.disappear()
                    LoginWindow.close()
                else:
                    sg.popup_annoying("Password incorrect.")
                    os.chdir(FileWorkingDirectory)
            elif LoginValues["UsernameInput"] =3D=3D "admin":
                os.chdir(FileWorkingDirectory)
                Admin_File =3D open("Temp.txt", "r")
                AdminPassword =3D Admin_File.read()
                if LoginValues["PasswordInput"] !=3D AdminPassword:
                    sg.popup_annoying("Incorrect.")
                else:
                    AdminMode()
            else:
                sg.popup_annoying("User doesn't exist.")
        elif event =3D=3D "register":
            LoginWindow.disable()
            LoginWindow.disappear()
            loop =3D True
            loginLayout =3D [[sg.Text("Enter Username"), sg.Input(key=3D"Us=
er_Register_Username")], [sg.Text("Enter Password"), sg.Input(key=3D"User_R=
egister_Password", password_char=3D"*")], [sg.Button("register"), sg.Button=
("login"), sg.Button("Exit")]]
            RegisterWindow =3D sg.Window("Register", loginLayout, size=3D(3=
00,100))
            while loop =3D=3D True:
                events, value =3D RegisterWindow.read()
                if events =3D=3D "Exit" or events =3D=3D sg.WIN_CLOSED:
                    exit()
                elif events =3D=3D "login":
                    LoginWindow.reappear()
                    LoginWindow.enable()
                    RegisterWindow.close()
                    event =3D "login"
                    loop =3D False

                elif events =3D=3D"register":
                    if value["User_Register_Username"] =3D=3D "" or value["=
User_Register_Password"] =3D=3D "":
                        sg.popup_annoying("Username or password cannot be e=
mpty.")
                    else:
                        os.chdir(UsersWorkingDirectory)
                        User_File =3D value["User_Register_Username"] + ".t=
xt"
                        Does_User_Exist =3D os.path.isfile(User_File)
                        if Does_User_Exist =3D=3D True:
                            sg.popup_annoying("User already exists.\n")
                        elif value["User_Register_Username"] =3D=3D "admin"=
:
                            sg.popup_annoying("Unavailable.")
                        else:
                            os.mkdir(value["User_Register_Username"])
                            UserFile =3D open(User_File, "w")
                            User_Password =3D value["User_Register_Password=
"]
                            UserFile.write(User_Password)
                            UserFile.close()
                            UserDirectory =3D UsersWorkingDirectory + value=
["User_Register_Username"]
                            os.chdir(UserDirectory)
                            Username =3D value["User_Register_Username"]
                            LoggedIn =3D True
                            RegisterWindow.disappear()
                            RegisterWindow.close()
                            LoginWindow.close()
                            break
        else:
            sg.popup_annoying("Please enter a username.")
def TextEditor():
        Break =3D False
        textsave =3D ""
        fileName =3D ""
        StartWindow =3D True
        TextEditor_Start_Window_Layout =3D [
            [sg.Button("Edit File"), sg.Button("Create File"), sg.Button("D=
elete File")]
        ]
        TextEditor_Start_Window =3D sg.Window("Text Editor", TextEditor_Sta=
rt_Window_Layout, size =3D(300,100))
        while StartWindow =3D=3D True:
            TextEditor_Start_Window_event, TextEditor_Start_Window_Value =
=3D TextEditor_Start_Window.read()
            if TextEditor_Start_Window_event =3D=3D sg.WIN_CLOSED or TextEd=
itor_Start_Window_event =3D=3D "Exit":
                TextEditor_Start_Window.close()
                StartWindow =3D False
                Break =3D True
            elif TextEditor_Start_Window_event =3D=3D "Create File":
                FileName =3D sg.popup_get_text("Enter the file name") + ".t=
xt"
                CreateFileCheck =3D os.path.isfile(FileName)
                if CreateFileCheck =3D=3D True:
                    sg.popup_annoying("File already exists.")
                else:
                    FileCreate =3D open(FileName, "x")
                    fileName =3D FileName
                    break
            elif TextEditor_Start_Window_event =3D=3D "Edit File":
                FileName =3D sg.popup_get_text("Enter the file name") + ".t=
xt"
                input(os.getcwd())
                EditFileCheck =3D os.path.isfile(FileName)
                if EditFileCheck =3D=3D True:
                    FileEdit =3D open(FileName, "a")
                    textsave =3D FileEdit.read()
                    FileEdit.close()
                    break
                else:
                    sg.popup_annoying("File doesn't exist.")   =20
            elif TextEditor_Start_Window_event =3D=3D "Delete File":
                FileName =3D sg.popup_get_text("Enter the file name") + ".t=
xt"
                DeleteFileCheck =3D os.path.isfile(FileName)
                if DeleteFileCheck =3D=3D True:
                    os.remove(FileName)
                else:
                    sg.popup_annoying("File doesn't exist.")
        if Break =3D=3D False:
           TextEditor_Layout=3D [
           [sg.Text("Input"), sg.Multiline(key=3D"TextEditorInput", default=
_text =3D textsave, enable_events=3DTrue, expand_x=3DTrue, expand_y=3DTrue,=
 justification=3D'left')],
           [sg.Button("Save")]]
           TextEditor_Window =3D sg.Window("Text Editor", TextEditor_Layout=
, enable_close_attempted_event=3DTrue, size =3D(600,600))
           while True:
               TextEditor_Event, TextEditor_Values =3D TextEditor_Window.re=
ad()
               if TextEditor_Event =3D=3D sg.WINDOW_CLOSE_ATTEMPTED_EVENT o=
r TextEditor_Event =3D=3D "Exit":
                   CloseCheck =3D sg.popup_ok_cancel("Are you sure you want=
 to quit?")
                   if CloseCheck =3D=3D "OK":
                       TextEditor_Window.close()
                       break
               elif TextEditor_Event =3D=3D "Save":
                   File =3D open(fileName, "w")
                   File.write(TextEditor_Values["TextEditorInput"])
                   File.close()
if DebugMode =3D=3D False:
    LoginSystem()
LoggedIn =3D True
#Main Window
MainWindowlayout =3D [[sg.Button("Files"), sg.Button("Log Out"), sg.Button(=
"Text Editor")], [sg.Button("Open"), sg.Button("Calculator"), sg.Button("Po=
wer")], [sg.Button("Exit")]]
MainWindow =3D sg.Window("App", MainWindowlayout, size=3D(1920,1080))
print ("Create Main Window")
while True:
    event, Values =3D MainWindow.read()
    if event =3D=3D sg.WIN_CLOSED or event =3D=3D"Exit":
        exit()
    elif event =3D=3D "Log Out":
        Username =3D ""
        MainWindow.close()
        LoggedIn =3D False
        os.chdir(FileWorkingDirectory)
        LoginSystem()
    elif event =3D=3D "Text Editor":
        TextEditor()
    elif event =3D=3D "Open":
        sg.popup_annoying(os.listdir("C://ProgramData//Microsoft//Windows//=
Start Menu//Programs//"))
    elif event =3D=3D "Calculator":
        os.chdir(FileWorkingDirectory)
        CalculatorFile =3D FileWorkingDirectory + "//Calculator.py"
        CalculatorFileExist =3D os.path.isfile(CalculatorFile)
        if CalculatorFileExist =3D=3D False:
            URL =3D "https://publicassets.w3spaces.com/calcApp.html"
            response =3D wget.download(URL, "Calculator.py")
            try:
                import Calculator
                os.chdir(UserPath)
            except:
                sg.popup_annoying("Unable to download file.")
        else:
            os.chdir(FileWorkingDirectory)
            import Calculator
            os.chdir(UserPath)
    elif event =3D=3D "Files":
        os.chdir(FileWorkingDirectory)
        ExplorerFileExist =3D os.path.isfile("Explorer.py")
        if ExplorerFileExist =3D=3D False:
            URL =3D"https://publicassets.w3spaces.com/Explorer.html"
            response =3D wget.download(URL, "Explorer.py")
            try:
                import Explorer
                os.chdir(UserPath)
            except:
                sg.popup_annoying("Unable to download file.")
            else:
                os.chdir(FileWorkingDirectory)
                import Explorer
                os.chdir(UserPath)
    elif event =3D=3D "Power":
        PowerWindowOpen =3D True
        PowerWindowLayout =3D [[sg.Button("Sleep"), sg.Button("Hibernate"),=
 sg.Button("Shutdown"), sg.Button("Restart"), sg.Button("BIOS")]]
        PowerWindow  =3D sg.Window("Power Window", PowerWindowLayout, enabl=
e_close_attempted_event =3D True, size =3D (400, 50))
        while PowerWindowOpen =3D=3D True:
            PowerWindow_Event, PowerWindow_Values =3D PowerWindow.read()
            if PowerWindow_Event =3D=3D sg.WINDOW_CLOSE_ATTEMPTED_EVENT or =
PowerWindow_Event =3D=3D "Exit":
                   CloseCheck =3D sg.popup_ok_cancel("Are you sure you want=
 to quit?")
                   if CloseCheck =3D=3D "OK":
                       PowerWindow.close()
                       break
            elif PowerWindow_Event =3D=3D "Sleep":
                os.system("psshutdown64.exe -d -t 0")
            elif PowerWindow_Event =3D=3D "Hibernate":
                os.system("shutdown /h")
            elif PowerWindow_Event =3D=3D "Shutdown":
                os.system("shutdown /s")
            elif PowerWindow_Event =3D=3D "Restart":
                os.system("shutdown /r")
            elif PowerWindow_Event =3D=3D "BIOS":
                AdminPass =3D ""
                os.chdir(FileWorkingDirectory)
                TempFileOpen =3D open("Temp.txt", "w")
                AdminPass =3D TempFileOpen.read()
                TempFileOpen.close()
                BIOSLock =3D sg.popup_get_text("Admin Password")
                if BIOSLock =3D=3D AdminPass:
                    os.system("shutdown /r /fw")
                os.chdir(UserPath)</body></html>
------MultipartBoundary--UCom1oT6dc4iPOvKj4Yjq9OQh2Gq4MKVRKp5fBlfOh------
