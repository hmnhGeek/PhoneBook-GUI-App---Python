import cx_Freeze

executables = [cx_Freeze.Executable('phonebook.py')]

cx_Freeze.setup(
    name='PhoneBook',
    options={"build_exe": {"packages":["Tkinter", "ttk", "PIL", "pickle", "os"
                                       , "tkMessageBox", "webbrowser", "tkFileDialog"
                                       , "shutil", "emailsending", "dictionary"
                                       , "changePhoto", "delfromDict", "contactmail", "changeDetails"],
                           "include_files":["account.dat", "contacts.dat", "contactView.png"
                                            , "createcontact.png", "delete.png", "developer.jpg"
                                            , "editwindow.png", "email.png", "home.png", "logo.png"
                                            , "menu.png", "remember_me.dat", "searchby.png", "searchbyemailid.png"
                                            , "searchbyname.png", "searchbyphno.png", "signup.png", "about.png", "contactmail.png"
                                            , "Whats new in v2.txt", "changedet.png", "cboth.png", "cpassw.png", "cuser.png"]}},

    description="PhoneBook",
    executables = executables
    )
