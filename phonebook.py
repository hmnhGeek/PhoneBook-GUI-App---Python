from Tkinter import*
import ttk
from PIL import ImageTk, Image
import pickle, os, tkMessageBox
import webbrowser
import tkFileDialog as tfd
import shutil
import emailsending as em
import dictionary as Dict
import changePhoto as cp
import delfromDict as dfd
import changeDetails as cngdet
import contactmail as cml

user_chose_a_photo = False
name_of_the_photo = ''
decision = []

root = Tk()
root.resizable(height = 0, width = 0)
root.title("Home")

f = open('remember_me.dat', 'rb')
try:
    while True:
        l = []
        l = pickle.load(f)
        decision = l
except:
    f.close()


def About():
    abtWin = Toplevel()
    abtWin.resizable(height = 0, width = 0)
    abtWin.title("About ePhoneBook")
    img = ImageTk.PhotoImage(Image.open('about.png'))
    panel = Label(abtWin, image = img)
    panel.pack(fill = 'both', expand = True)

    img1 = ImageTk.PhotoImage(Image.open('developer.jpg'))
    panel = Label(abtWin, image = img1)
    panel.pack(fill = 'both', expand = True)
    panel.place(x = 30, y = 140)

    def callback(event):
        webbrowser.open('http://www.twitter.com/hmnhsharma/')

    follow = Label(abtWin, text = 'Follow Himanshu Sharma', font = ('Arial', 15), cursor = 'hand2', bg = 'white',
                   fg = 'red')
    follow.pack()
    follow.place(x = 770, y = 230)
    follow.bind('<Button-1>', callback)
    
    abtWin.mainloop()

def go():
    webbrowser.open('http://hmnhsharma974.wix.com/mysite')

def forgotMyPassword():
    root.iconify()
    helpMe = Toplevel()
    helpMe.resizable(height = 0, width = 0)
    helpMe.title("Forgot your details...")
    img1 = ImageTk.PhotoImage(Image.open('email.png'))
    panel = Label(helpMe, image = img1)
    panel.pack(fill = 'both', expand = True)

    emailid = ttk.Entry(helpMe, width = 40)
    emailid.pack()
    emailid.place(x = 500, y = 135)

    emailidP = ttk.Entry(helpMe, width = 40, show = 'x')
    emailidP.pack()
    emailidP.place(x = 500, y = 210)

    server = ttk.Entry(helpMe, width = 40)
    server.pack()
    server.place(x = 500, y = 270)

    port = ttk.Entry(helpMe, width = 40)
    port.pack()
    port.place(x = 500, y = 330)

    def callback(event):
        if emailid.get() <> '':
            site = ''
            rev = emailid.get()[-1:-len(emailid.get())-1:-1]
            for i in rev:
                if i == '@':
                    break
                else:
                    site+=i
            site = site[-1:-len(site)-1:-1]

            webbrowser.open('https://www.google.com/#q=smtp+server+and+port+for+'+site)
        else:
            tkMessageBox.showinfo("Alert", "Please enter your Email ID, so that we can find you the details.")

    serverLabel = Label(helpMe, text = "Find my server and port", font = ('Arial', 15), cursor = 'hand2', bg = 'white'
                        ,fg = 'blue')
    serverLabel.pack()
    serverLabel.place(x = 530, y = 385)
    serverLabel.bind('<Button-1>', callback)

    def logINMyMail():

        dq = Dict.returnDictionary('account.dat')
        dp = Dict.returnDictionary('contacts.dat')

        user = dq.keys()[0]
        passu = dq[user]

    
        if emailid.get() == '' or emailidP.get() == '':
            tkMessageBox.showinfo("Alert", "Please enter email id and password.")
        else:
                
            if server.get() == '' or port.get() == '':
                if em.start_server(emailid.get(), emailidP.get(), 'hmnhsharma97@gmail.com', user+' '+passu) == 1:
                    tkMessageBox.showinfo("Alert", "Your problem has been sent to developer.")
                elif em.start_server(emailid.get(), emailidP.get(), 'hmnhsharma97@gmail.com', user+' '+passu) == 0:
                    tkMessageBox.showwarning("Alert", "Either Email ID or Password is wrong.")
                else:
                    tkMessageBox.showwarning("Alert", "Internet not working, check your connection.")
            else:
                if em.start_server(emailid.get(), emailidP.get(), 'hmnhsharma97@gmail.com', user+' '+passu, server.get(), int(port.get())) == 1:
                    tkMessageBox.showinfo("Alert", "Your problem has been sent to developer.")
                elif em.start_server(emailid.get(), emailidP.get(), 'hmnhsharma97@gmail.com', user+' '+passu, server.get(), int(port.get())) == 0:
                    tkMessageBox.showwarning("Alert", "Either Email ID or Password is wrong.")
                else:
                    tkMessageBox.showwarning("Alert", "Internet not working, check your connection.")

    createButton = Button(helpMe, text = "Continue", bg = "green", bd = 0, width = 14,height = 1,
                          font = ("Arial", 18)
                          , activebackground = 'green', command = logINMyMail,
                          activeforeground = "White", fg = "White")
    createButton.pack()
    createButton.place(x = 300, y = 385)
    
    
    helpMe.mainloop()


def cng():
    root.iconify()
    changingWindow = Toplevel()
    changingWindow.resizable(height = 0, width = 0)
    changingWindow.title("Change your details...")
    
    img1 = ImageTk.PhotoImage(Image.open('changedet.png'))
    panel = Label(changingWindow, image = img1)
    panel.pack(fill = 'both', expand = True)

    Id = ttk.Entry(changingWindow, width = 40)
    Id.pack()
    Id.place(x = 460, y = 135)

    passw = ttk.Entry(changingWindow, width = 40, show = 'x')
    passw.pack()
    passw.place(x = 460, y = 240)


    def change():
        obj = cngdet.changeDetails(Id.get(), passw.get(), 'account.dat')

        if obj.check():
            changingWindow.destroy()
            mainchang = Toplevel()
            mainchang.title('Choose a category...')
            mainchang.resizable(height = 0, width = 0)

            img1 = ImageTk.PhotoImage(Image.open('searchby.png'))
            panel = Label(mainchang, image = img1)
            panel.pack(fill = 'both', expand = True)

            def cuser():
                mainchang.destroy()
                ciserWin = Toplevel()

                img1 = ImageTk.PhotoImage(Image.open('cuser.png'))
                panel = Label(ciserWin, image = img1)
                panel.pack(fill = 'both', expand = True)

                newid = ttk.Entry(ciserWin, width = 50)
                newid.pack()
                newid.place(x = 350, y = 210)

                def done():
                    obj.changeUsername(newid.get())
                    tkMessageBox.showinfo("Alert", "Username changed successfully.")
                    ciserWin.destroy()

                changeB = Button(ciserWin, text = "Change", bg = "green", bd = 0, width = 14,height = 1,
                          font = ("Arial", 18)
                          , activebackground = 'green', command = done,
                          activeforeground = "White", fg = "White")
                changeB.pack()
                changeB.place(x = 400, y = 385)

                ciserWin.mainloop()

            def cpassw():
                mainchang.destroy()
                ciserWin = Toplevel()

                img1 = ImageTk.PhotoImage(Image.open('cpassw.png'))
                panel = Label(ciserWin, image = img1)
                panel.pack(fill = 'both', expand = True)

                newpass = ttk.Entry(ciserWin, width = 50, show = 'x')
                newpass.pack()
                newpass.place(x = 350, y = 210)

                def done():
                    obj.changePassword(newpass.get())
                    tkMessageBox.showinfo("Alert", "Password changed successfully.")
                    ciserWin.destroy()

                changeB = Button(ciserWin, text = "Change", bg = "green", bd = 0, width = 14,height = 1,
                          font = ("Arial", 18)
                          , activebackground = 'green', command = done,
                          activeforeground = "White", fg = "White")
                changeB.pack()
                changeB.place(x = 400, y = 385)

                ciserWin.mainloop()

            def cboth():
                mainchang.destroy()
                ciserWin = Toplevel()

                img1 = ImageTk.PhotoImage(Image.open('cboth.png'))
                panel = Label(ciserWin, image = img1)
                panel.pack(fill = 'both', expand = True)

                newid = ttk.Entry(ciserWin, width = 50)
                newid.pack()
                newid.place(x = 350, y = 180)

                newpass = ttk.Entry(ciserWin, width = 50, show = 'x')
                newpass.pack()
                newpass.place(x = 350, y = 310)

                def done():
                    obj.changeBoth(newid.get(), newpass.get())
                    tkMessageBox.showinfo("Alert", "Username and Password both changed successfully.")
                    ciserWin.destroy()

                changeB = Button(ciserWin, text = "Change", bg = "green", bd = 0, width = 14,height = 1,
                          font = ("Arial", 18)
                          , activebackground = 'green', command = done,
                          activeforeground = "White", fg = "White")
                changeB.pack()
                changeB.place(x = 400, y = 385)

                ciserWin.mainloop()

                
            var = IntVar()
            R1 = Radiobutton(mainchang, text="Change Username only", variable=var, value=1, command=cuser,
                             bg = 'white', font = ("Arial", 18), activebackground = 'white')
            R1.pack( anchor = W )
            R1.place(x = 300, y = 100)

            R2 = Radiobutton(mainchang, text="Change Password only", variable=var, value=2, command=cpassw,
                             bg = 'white', font = ("Arial", 18), activebackground = 'white')
            R2.pack( anchor = W )
            R2.place(x = 300, y = 150)

            R3 = Radiobutton(mainchang, text="Change Both", variable=var, value=3, command=cboth,
                             bg = 'white', font = ("Arial", 18), activebackground = 'white')
            R3.pack( anchor = W )
            R3.place(x = 300, y = 200)

            mainchang.mainloop()
            
        else:
            tkMessageBox.showinfo("Alert", "Something is wrong!!")

    changeB = Button(changingWindow, text = "Continue", bg = "green", bd = 0, width = 14,height = 1,
                          font = ("Arial", 18)
                          , activebackground = 'green', command = change,
                          activeforeground = "White", fg = "White")
    changeB.pack()
    changeB.place(x = 400, y = 385)
    
    
    changingWindow.mainloop()

def newinv2():
    root.iconify()
    whatswin = Toplevel()
    whatswin.resizable(height = 0, width = 0)
    whatswin.title("What's new in version 2 of ePhoneBook...")

    scrollbar = Scrollbar(whatswin)
    scrollbar.pack(side = RIGHT, fill = Y)
    area = Text(whatswin, yscrollcommand = scrollbar.set)
    area.pack()

    File = open('Whats new in v2.txt', 'r')
    s = File.read()
    File.close()

    area.insert(END, s)

    scrollbar.config(command = area.yview)
    area.config(state = DISABLED)

    whatswin.mainloop()

menubar = Menu(root)
filemenu = Menu(menubar, tearoff = 0)
filemenu.add_command(label = "About", command = About)
filemenu.add_separator()
filemenu.add_command(label = "Exit", command = root.destroy)

filemenu1 = Menu(menubar, tearoff = 0)
filemenu1.add_command(label = "Go to http://hmnhsharma974.wix.com/mysite for more apps", command = go)
filemenu1.add_separator()

filemenu2 = Menu(menubar, tearoff = 0)
filemenu2.add_command(label = "Forgot my details", command = forgotMyPassword)
filemenu2.add_command(label = "Change my login details", command = cng)
filemenu2.add_separator()
filemenu2.add_command(label = "What's new in v2?", command = newinv2)

menubar.add_cascade(label = "File", menu = filemenu)
menubar.add_cascade(label = "More Apps", menu = filemenu1)
menubar.add_cascade(label = "Help", menu = filemenu2)

root.config(menu = menubar)

img = ImageTk.PhotoImage(Image.open('home.png'))
panel = Label(root, image = img)
panel.pack(fill = 'both', expand = True)

ID = ttk.Entry(root, width = 40)
ID.pack()
ID.place(x = 450, y = 140)

password = ttk.Entry(root, width = 40, show = 'x')
password.pack()
password.place(x = 450, y = 185)

if decision[0]:
    
    f = open('account.dat', 'rb')
    try:
        while True:
            data = {}
            data = pickle.load(f)
            username = data.keys()
            
            PASSWORD = data[username[0]]
            USERNAME = username[0]
    except:
        f.close()

    ID.insert(0, USERNAME)
    password.insert(0, PASSWORD)

def login():
    f = open('account.dat', 'rb')

    try:
        while True:
            d = {}
            d = pickle.load(f)

            if d.has_key(ID.get()):
                if d[ID.get()] == password.get():
                    root.destroy()
                    phonebook = Tk()
                    phonebook.resizable(height = 0, width = 0)
                    phonebook.title("Your Phonebook")

                    img = ImageTk.PhotoImage(Image.open('menu.png'))
                    panel = Label(phonebook, image = img)
                    panel.pack(fill = 'both', expand = True)

                    def go():
                        webbrowser.open('http://hmnhsharma974.wix.com/mysite')

                    def view():
                        f1 = open('contacts.dat', 'rb')
                        phonebook.iconify()
                        allContactsWin = Toplevel()
                        allContactsWin.resizable(height = 0, width = 0)
                        allContactsWin.title("All Contacts")

                        scrollbar = Scrollbar(allContactsWin)
                        scrollbar.pack(side = RIGHT, fill = Y)
                        area = Text(allContactsWin, yscrollcommand = scrollbar.set)
                        area.pack()
                        
                        try:
                            while True:
                                contacts = {}
                                contacts = pickle.load(f1)
                                if contacts == {}:
                                    area.insert(END, 'No records found.')
                                else:
                                    for each_phone_number in contacts:
                                                    
                                        area.insert(END, '---------------------\n')
                                        area.insert(END, 'Ph. Number: '+each_phone_number+'\n')
                                        area.insert(END, 'Name: '+contacts[each_phone_number][0]+'\n')
                                        area.insert(END, 'Email ID: '+contacts[each_phone_number][1]+'\n')
                                        area.insert(END, 'Photo Status: '+str(contacts[each_phone_number][2][0])+'\n')
                                    
                        except:
                            f.close()
                        scrollbar.config(command = area.yview)
                        area.config(state = DISABLED)
                        allContactsWin.mainloop()

                    def delete():
                        phonebook.iconify()
                        deleteWin = Toplevel()
                        deleteWin.resizable(height = 0, width = 0)
                        deleteWin.title("Delte a contact")
                        
                        img = ImageTk.PhotoImage(Image.open('searchbyphno.png'))
                        panel = Label(deleteWin, image = img)
                        panel.pack(fill = 'both', expand = True)

                        fone_number = ttk.Entry(deleteWin, width = 50)
                        fone_number.pack()
                        fone_number.place(x = 350, y = 200)

                        def Del():
                            module0bj = dfd.delfromDict('contacts.dat')
                            module0bj.delete(fone_number.get())
                            deleteWin.destroy()

                        searchNow = Button(deleteWin, text = "Search", bg = "green", bd = 0,
                                           width = 10, height = 2,font = ("Arial", 18)
                                           , activebackground = 'green', command = Del,
                                           activeforeground = "White", fg = "White")
                        searchNow.pack()
                        searchNow.place(x = 425, y = 315)

                        deleteWin.mainloop()

                    def manage():
                        rem = open('remember_me.dat', 'rb')
                        remw = open('temp.dat', 'wb')

                        try:
                            while True:
                                decision = []
                                decision = pickle.load(rem)
                                
                                if not decision[0]:
                                    if tkMessageBox.askyesno("Alert", "Do you want to save your login ID and password?"):
                                        decision[0] = True
                                        pickle.dump(decision, remw)
                                    else:
                                        pickle.dump(decision, remw)
                                else:
                                    if tkMessageBox.askyesno("Alert", "Do you want to make me forget your login ID and password?"):
                                        decision[0] = False
                                        pickle.dump(decision, remw)
                                    else:
                                        pickle.dump(decision, remw)
                        except:
                            rem.close()
                        remw.close()
                        os.remove('remember_me.dat')
                        os.rename('temp.dat', 'remember_me.dat')

                    menubar = Menu(phonebook)
                    filemenu = Menu(menubar, tearoff = 0)
                    filemenu.add_command(label = "View all contacts", command = view)
                    filemenu.add_command(label = "Manage Login", command = manage)
                    filemenu.add_command(label = "Delete a contact", command = delete)
                    filemenu.add_separator()
                    filemenu.add_command(label = "Exit", command = phonebook.destroy)

                    filemenu1 = Menu(menubar, tearoff = 0)
                    filemenu1.add_command(label = "Go to http://hmnhsharma974.wix.com/mysite for more apps", command = go)
                    filemenu1.add_separator()

                    menubar.add_cascade(label = "File", menu = filemenu)
                    menubar.add_cascade(label = "More Apps", menu = filemenu1)

                    phonebook.config(menu = menubar)


                    def add():
                        phonebook.iconify()
                        createContactWindow = Toplevel()
                        createContactWindow.resizable(height = 0, width = 0)
                        createContactWindow.title("Create a contact")
                        
                        img = ImageTk.PhotoImage(Image.open('createcontact.png'))
                        panel = Label(createContactWindow, image = img)
                        panel.pack(fill = 'both', expand = True)

                        name = ttk.Entry(createContactWindow, width = 50)
                        name.pack()
                        name.place(x = 380, y = 120)

                        phno = ttk.Entry(createContactWindow, width = 40)
                        phno.pack()
                        phno.place(x = 460, y = 190)

                        email = ttk.Entry(createContactWindow, width = 40)
                        email.pack()
                        email.place(x = 420, y = 265)


                        def choose():
                            global user_chose_a_photo
                            global name_of_the_photo
                            if name.get() <> '' and phno.get() <> '':
                                try:
                                    shutil.copyfile('contacts.dat', 'copied.dat')
                                    f = tfd.askopenfile()
                                    s = f.name
                                    f.close()

                                    extension = ''

                                    reverse = s[-1:-len(s)-1:-1]

                                    for i in reverse:
                                        if i<>"/":
                                            extension+=i
                                        else:
                                            break

                                    name_of_the_photo = extension[-1:-len(extension)-1:-1]

                                    shutil.copyfile(s, '%imgs//'+extension[-1:-len(extension)-1:-1])
                                    user_chose_a_photo = True
                                    os.remove('copied.dat')
                
                                except:
                                    createContactWindow.destroy()
                                    os.remove('contacts.dat')
                                    os.rename('copied.dat', 'contacts.dat')
                                    
                            else:
                                tkMessageBox.showwarning("Alert", "Choose photo after entering name and phone number only.")

                        def create():
                            global user_chose_a_photo
                            global name_of_the_photo
                            if name.get() <> '' and phno.get() <> '':
                                f1 = open('contacts.dat', 'rb')
                                f2 = open('temp.dat', 'wb')

                                try:
                                    while True:
                                        contacts = {}
                                        contacts = pickle.load(f1)

                                        if phno.get() in contacts:
                                            tkMessageBox.showinfo("Alert", "This contact already exists.")
                                            pickle.dump(contacts, f2)
                                        else:
                                            contacts.update({phno.get():[name.get(), email.get(), [user_chose_a_photo,
                                                                                                   name_of_the_photo
                                                                                                   ]]})
                                            pickle.dump(contacts, f2)
                                            tkMessageBox.showinfo("Alert", "Contact created!!")
                                            createContactWindow.destroy()
                                except:
                                    f1.close()
                                f2.close()
                                os.remove('contacts.dat')
                                os.rename('temp.dat', 'contacts.dat')
                            else:
                                tkMessageBox.showwarning("Alert", "Either Name field or Phone Number field is missing.")
                                        

                        choosephotoButton = ttk.Button(createContactWindow, text = "Choose Photo", command = choose)
                        choosephotoButton.pack()
                        choosephotoButton.place(x = 550, y = 340)

                        createButton = Button(createContactWindow, text = "Create Contact", bg = "green", bd = 0, width = 14,
                                              height = 1,
                                       font = ("Arial", 18)
                                              , activebackground = 'green', command = create,
                                              activeforeground = "White", fg = "White")
                        createButton.pack()
                        createButton.place(x = 400, y = 385)
                        
                        createContactWindow.mainloop()

                    def edit_a_contact():
                        phonebook.iconify()

                        editWin = Toplevel()
                        editWin.resizable(height = 0, width = 0)
                        editWin.title("Edit a contact")

                        img = ImageTk.PhotoImage(Image.open('searchbyphno.png'))
                        panel = Label(editWin, image = img)
                        panel.pack(fill = 'both', expand = True)

                        phoneNumber = ttk.Entry(editWin, width = 50)
                        phoneNumber.pack()
                        phoneNumber.place(x = 350, y = 200)

                        def openit():
                            f = open('contacts.dat', 'rb')

                            try:
                                while True:
                                    contacts = {}
                                    contacts = pickle.load(f)

                                    if phoneNumber.get() in contacts:
                                        f.close()
                                        editWin.iconify()
                                        
                                        mainEditWindow = Toplevel()
                                        mainEditWindow.resizable(height = 0, width = 0)
                                        mainEditWindow.title("Edit a contact")

                                        imgA = ImageTk.PhotoImage(Image.open('editwindow.png'))
                                        panel = Label(mainEditWindow, image = imgA)
                                        panel.pack(fill = 'both', expand = True)

                                        data_of_contact = contacts[phoneNumber.get()]
                                            
                                        name_of_the_contact = data_of_contact[0]
                                        emailid_of_the_contact = data_of_contact[1]
                                        user_chose_a_photo = data_of_contact[2][0]
                                        name_of_the_image = data_of_contact[2][1]

                                        nameEntry = ttk.Entry(mainEditWindow, width = 40)
                                        nameEntry.pack()
                                        nameEntry.place(x = 610, y = 110)
                                        nameEntry.insert(0, name_of_the_contact)

                                        phoneNumEntry = ttk.Entry(mainEditWindow, width = 40)
                                        phoneNumEntry.pack()
                                        phoneNumEntry.place(x = 720, y = 215)
                                        phoneNumEntry.insert(0, phoneNumber.get())

                                        emailEntry = ttk.Entry(mainEditWindow, width = 40)
                                        emailEntry.pack()
                                        emailEntry.place(x = 650, y = 320)
                                        emailEntry.insert(0, emailid_of_the_contact)

                                        if user_chose_a_photo:
                                            img1 = ImageTk.PhotoImage(Image.open("%imgs\\"+name_of_the_image))
                                            photoLabel = Label(mainEditWindow, image = img1)
                                            photoLabel.pack(expand = True, fill = 'both')
                                            photoLabel.place(x = 100, y = 100)
                                        else:
                                            img1 = ImageTk.PhotoImage(Image.open("%imgs\\sparephoto.png"))
                                            photoLabel = Label(mainEditWindow, image = img1)
                                            photoLabel.pack(expand = True, fill = 'both')
                                            photoLabel.place(x = 100, y = 100)

                                        def save():
                                            f = open('contacts.dat','rb')
                                            fw = open('temp.dat', 'wb')

                                            try:
                                                while True:
                                                    contacts = {}
                                                    contacts = pickle.load(f)
                                                    del contacts[phoneNumber.get()]
                                                    contacts.update({phoneNumEntry.get():[nameEntry.get(),
                                                                                 emailEntry.get(), [user_chose_a_photo,
                                                                                                           name_of_the_image
                                                                                                           ]]})
                                                    pickle.dump(contacts, fw)
                                                    tkMessageBox.showinfo("Alert", "Contact updated.")
                                                    mainEditWindow.destroy()
                                                    editWin.destroy()
                                            except:
                                                f.close()
                                            fw.close()
                                            os.remove('contacts.dat')
                                            os.rename('temp.dat', 'contacts.dat')

                                        def changePic():
                                            cp.changePhoto(phoneNumber.get())
                                            tkMessageBox.showinfo("Alert", "New photo updated!!")
                                            mainEditWindow.destroy()
                                            editWin.destroy()
                            
                                        SaveButton = Button(mainEditWindow, text = "Save", bg = "grey", bd = 0,
                                           width = 8, height = 1,font = ("Arial", 18)
                                           , activebackground = 'grey', command = save,
                                           activeforeground = "White", fg = "White")
                                        SaveButton.pack()
                                        SaveButton.place(x = 580, y = 415)

                                        changePhotoButton = Button(mainEditWindow, text = "Change Photo", bg = "grey", bd = 0,
                                           width = 12, height = 1,font = ("Arial", 18)
                                           , activebackground = 'grey', command = changePic,
                                           activeforeground = "White", fg = "White")
                                        changePhotoButton.pack()
                                        changePhotoButton.place(x = 780, y = 415)

                                        mainEditWindow.mainloop()
                                        
                                        
                                    else:
                                        tkMessageBox.showwarning("Alert", "No such phone number in records.")
                                        
                            except:
                                f.close()

                        searchNow = Button(editWin, text = "Search", bg = "green", bd = 0,
                                           width = 10, height = 2,font = ("Arial", 18)
                                           , activebackground = 'green', command = openit,
                                           activeforeground = "White", fg = "White")
                        searchNow.pack()
                        searchNow.place(x = 425, y = 315)

                        editWin.mainloop()

                    def searchC():
                        phonebook.iconify()
                        searchby = Toplevel()
                        searchby.resizable(height = 0, width = 0)
                        searchby.title("Search by window")
                        
                        img = ImageTk.PhotoImage(Image.open('searchby.png'))
                        panel = Label(searchby, image = img)
                        panel.pack(fill = 'both', expand = True)

                        def sbyphno():
                            searchby.destroy()
                            searchbyphnoWindow = Toplevel()
                            searchbyphnoWindow.resizable(height = 0, width = 0)
                            searchbyphnoWindow.title("Search a contact by phone number")
                            img = ImageTk.PhotoImage(Image.open('searchbyphno.png'))
                            panel = Label(searchbyphnoWindow, image = img)
                            panel.pack(fill = 'both', expand = True)

                            phoneNumber = ttk.Entry(searchbyphnoWindow, width = 50)
                            phoneNumber.pack()
                            phoneNumber.place(x = 350, y = 200)

                            def searching():
                                f = open("contacts.dat", "rb")

                                try:
                                    while True:
                                        contacts = {}
                                        contacts = pickle.load(f)

                                        if phoneNumber.get() in contacts:
                                            f.close()
                                            fone = phoneNumber.get()
                                            searchbyphnoWindow.destroy()
                                            
                                            phoneBookView = Toplevel()
                                            phoneBookView.resizable(height = 0, width = 0)
                                            phoneBookView.title("PhoneBook")

                                            img = ImageTk.PhotoImage(Image.open('contactView.png'))
                                            panel = Label(phoneBookView, image = img)
                                            panel.pack(fill = 'both', expand = True)

                                            data_of_contact = contacts[fone]
                                            
                                            name_of_the_contact = data_of_contact[0]
                                            emailid_of_the_contact = data_of_contact[1]
                                            user_chose_a_photo = data_of_contact[2][0]
                                            name_of_the_image = data_of_contact[2][1]

                                            nameLabel = Label(phoneBookView, text = name_of_the_contact,
                                                              font = ("Arial", 18), bg = 'yellow')
                                            nameLabel.pack()
                                            nameLabel.place(x = 610, y = 110)

                                            phonenumberLabel = Label(phoneBookView, text = fone,
                                                              font = ("Arial", 18), bg = 'yellow')
                                            phonenumberLabel.pack()
                                            phonenumberLabel.place(x = 720, y = 215)

                                            def callback(event):
                                                to = emailidlabel['text']
                                                
                                                phoneBookView.iconify()
                                                sendmail = Toplevel()
                                                sendmail.resizable(height = 0, width = 0)
                                                sendmail.title("Send a mail")
                                                
                                                img = ImageTk.PhotoImage(Image.open('email.png'))
                                                panel = Label(sendmail, image = img)
                                                panel.pack(fill = 'both', expand = True)

                                                emailid = ttk.Entry(sendmail, width = 40)
                                                emailid.pack()
                                                emailid.place(x = 500, y = 135)

                                                emailidP = ttk.Entry(sendmail, width = 40, show = 'x')
                                                emailidP.pack()
                                                emailidP.place(x = 500, y = 210)

                                                server = ttk.Entry(sendmail, width = 40)
                                                server.pack()
                                                server.place(x = 500, y = 270)

                                                port = ttk.Entry(sendmail, width = 40)
                                                port.pack()
                                                port.place(x = 500, y = 330)

                                                def call(event):
                                                    if emailid.get() <> '':
                                                        site = ''
                                                        rev = emailid.get()[-1:-len(emailid.get())-1:-1]
                                                        for i in rev:
                                                            if i == '@':
                                                                break
                                                            else:
                                                                site+=i
                                                        site = site[-1:-len(site)-1:-1]

                                                        webbrowser.open('https://www.google.com/#q=smtp+server+and+port+for+'+site)
                                                    else:
                                                        tkMessageBox.showinfo("Alert", "Please enter your Email ID, so that we can find you the details.")

                                                serverLabel = Label(sendmail, text = "Find my server and port", font = ('Arial', 15), cursor = 'hand2', bg = 'white'
                                                                    ,fg = 'blue')
                                                serverLabel.pack()
                                                serverLabel.place(x = 530, y = 385)
                                                serverLabel.bind('<Button-1>', call)

                                                def cont(event):
                                                    if server.get() == '' or port.get() == '':
                                                        if cml.check_credentials(emailid.get(), emailidP.get()) == 1:
                                                            ID = emailid.get()
                                                            Pass = emailidP.get()
                                                            sendmail.destroy()
                                                            mainmail = Toplevel()
                                                            mainmail.resizable(height = 0, width = 0)
                                                            mainmail.title("Mail on the way...")

                                                            img1 = ImageTk.PhotoImage(Image.open("contactmail.png"))
                                                            photoLabel = Label(mainmail, image = img1)
                                                            photoLabel.pack(expand = True, fill = 'both')

                                                            scrollbar = Scrollbar(phoneBookView)
                                                            scrollbar.pack(side = RIGHT, fill = Y)
                                                            area = Text(mainmail, yscrollcommand = scrollbar.set, width = 50, height = 20, bd = 3)
                                                            area.pack()
                                                            area.place(x = 300, y = 70)

                                                            def sendit(event):
                                                                msg = area.get(1.0, END)
                                                                em.start_server(ID, Pass, to, msg)
                                                                tkMessageBox.showinfo("Alert", "Your message has been sent.")

                                                                mainmail.destroy()
                                                                
                                                            scrollbar.config(command = area.yview)

                                                            send = Label(mainmail, text = 'Send to '+to, font = ('Arial', 15), cursor = 'hand2', bg = 'white',
                                                                         fg = 'blue')
                                                            send.pack()
                                                            send.place(x = 400, y = 400)
                                                            send.bind('<Button-1>', sendit)
                                                            
                                                            mainmail.mainloop()
                                                            
                                                        elif cml.check_credentials(emailid.get(), emailidP.get()) == 0:
                                                            tkMessageBox.showwarning("Alert", "Wrong username or password.")

                                                        else:
                                                            tkMessageBox.showwarning("Alert", "Internet not working, check your connection.")
                                                    else:
                                                        if cml.check_credentials(emailid.get(), emailidP.get(), server.get(), port.get()) == 1:
                                                            ID = emailid.get()
                                                            Pass = emailidP.get()
                                                            SERVER = server.get()
                                                            PORT = port.get()
                                                            sendmail.destroy()
                                                            mainmail = Toplevel()
                                                            mainmail.resizable(height = 0, width = 0)
                                                            mainmail.title("Mail on the way...")

                                                            img1 = ImageTk.PhotoImage(Image.open("contactmail.png"))
                                                            photoLabel = Label(mainmail, image = img1)
                                                            photoLabel.pack(expand = True, fill = 'both')

                                                            scrollbar = Scrollbar(phoneBookView)
                                                            scrollbar.pack(side = RIGHT, fill = Y)
                                                            area = Text(mainmail, yscrollcommand = scrollbar.set, width = 50, height = 20, bd = 3)
                                                            area.pack()
                                                            area.place(x = 300, y = 70)

                                                            def sendit(event):
                                                                msg = area.get(1.0, END)
                                                                em.start_server(ID, Pass, to, msg, SERVER, int(PORT))
                                                                tkMessageBox.showinfo("Alert", "Your message has been sent.")

                                                                mainmail.destroy()
                                                                
                                                            scrollbar.config(command = area.yview)

                                                            send = Label(mainmail, text = 'Send to '+to, font = ('Arial', 15), cursor = 'hand2', bg = 'white',
                                                                         fg = 'blue')
                                                            send.pack()
                                                            send.place(x = 400, y = 400)
                                                            send.bind('<Button-1>', sendit)
                                                            
                                                            mainmail.mainloop()

                                                        elif cml.check_credentials(emailid.get(), emailidP.get(), server.get(), port.get()) == 0:
                                                            tkMessageBox.showwarning("Alert", "Wrong username or password or maybe server or port are wrong.")

                                                        else:
                                                            tkMessageBox.showwarning("Alert", "Internet not working, check your connection.")
                                                continueLink = Label(sendmail, text = "Continue", font = ('Arial', 15), cursor = 'hand2', bg = 'white'
                                                                    ,fg = 'blue')
                                                continueLink.pack()
                                                continueLink.place(x = 300, y = 385)
                                                continueLink.bind('<Button-1>', cont)
                                                
                                                sendmail.mainloop()

                                            emailidlabel = Label(phoneBookView, text = emailid_of_the_contact,
                                                              font = ("Arial", 18), bg = 'yellow', cursor = 'hand2', fg = 'blue')
                                            emailidlabel.pack()
                                            emailidlabel.place(x = 650, y = 320)
                                            emailidlabel.bind('<Button-1>', callback)

                                            if user_chose_a_photo:
                                                img1 = ImageTk.PhotoImage(Image.open("%imgs\\"+name_of_the_image))
                                                photoLabel = Label(phoneBookView, image = img1)
                                                photoLabel.pack(expand = True, fill = 'both')
                                                photoLabel.place(x = 100, y = 100)
                                            else:
                                                img1 = ImageTk.PhotoImage(Image.open("%imgs\\sparephoto.png"))
                                                photoLabel = Label(phoneBookView, image = img1)
                                                photoLabel.pack(expand = True, fill = 'both')
                                                photoLabel.place(x = 100, y = 100)

                                            phoneBookView.mainloop()
                                            
                                        else:
                                            tkMessageBox.showinfo("Alert", "No such phone number in records.")
                                except:
                                    f.close()

                            searchNow = Button(searchbyphnoWindow, text = "Search", bg = "green", bd = 0,
                                               width = 10, height = 2,
                                            font = ("Arial", 18)
                                            , activebackground = 'green', command = searching,
                                               activeforeground = "White", fg = "White")
                            searchNow.pack()
                            searchNow.place(x = 425, y = 315)

                            searchbyphnoWindow.mainloop()

                        def sbyname():
                            searchby.destroy()
                            searchbyNameWindow = Toplevel()
                            searchbyNameWindow.resizable(height = 0, width = 0)
                            searchbyNameWindow.title("Search a contact by name")
                            
                            img = ImageTk.PhotoImage(Image.open('searchbyname.png'))
                            panel = Label(searchbyNameWindow, image = img)
                            panel.pack(fill = 'both', expand = True)

                            nameEnter = ttk.Entry(searchbyNameWindow, width = 50)
                            nameEnter.pack()
                            nameEnter.place(x = 350, y = 200)

                            def searching():
                                name = nameEnter.get()
                                searchbyNameWindow.destroy()
                                phoneBookView = Tk()
                                phoneBookView.resizable(height = 0, width = 0)
                                phoneBookView.title('PhoneBook')

                                scrollbar = Scrollbar(phoneBookView)
                                scrollbar.pack(side = RIGHT, fill = Y)
                                area = Text(phoneBookView, yscrollcommand = scrollbar.set)
                                area.pack()
                                
                                f = open('contacts.dat', 'rb')
                                found = 0
                                try:
                                    while True:
                                        
                                        contacts = {}
                                        contacts = pickle.load(f)
                                        
                                        for each_phone_number in contacts:
                                            if contacts[each_phone_number][0] == name:
                                                found += 1
                                                area.insert(END, '---------------------\n')
                                                area.insert(END, 'Ph. Number: '+each_phone_number+'\n')
                                                area.insert(END, 'Email ID: '+contacts[each_phone_number][1]+'\n')
                                                area.insert(END, 'Photo Status: '+str(contacts[each_phone_number][2][0])+'\n')
                                        if found == 0:
                                            area.insert(END, "No record found.")
                                except:
                                    f.close()
                                scrollbar.config(command = area.yview)
                                area.config(state = DISABLED)
                                phoneBookView.mainloop()

                            searchNow = Button(searchbyNameWindow, text = "Search", bg = "green", bd = 0,
                                               width = 10, height = 2,
                                            font = ("Arial", 18)
                                            , activebackground = 'green', command = searching,
                                               activeforeground = "White", fg = "White")
                            searchNow.pack()
                            searchNow.place(x = 425, y = 315)
                            
                            searchbyNameWindow.mainloop()
                            

                        def sbyemailid():
                            searchby.destroy()
                            searchbyEmailIDWindow = Toplevel()
                            searchbyEmailIDWindow.resizable(height = 0, width = 0)
                            searchbyEmailIDWindow.title("Search a contact by name")
                            
                            img = ImageTk.PhotoImage(Image.open('searchbyemailid.png'))
                            panel = Label(searchbyEmailIDWindow, image = img)
                            panel.pack(fill = 'both', expand = True)

                            emailidenter = ttk.Entry(searchbyEmailIDWindow, width = 50)
                            emailidenter.pack()
                            emailidenter.place(x = 350, y = 200)

                            def searching():
                                email = emailidenter.get()
                                searchbyEmailIDWindow.destroy()
                                phoneBookView = Tk()
                                phoneBookView.resizable(height = 0, width = 0)
                                phoneBookView.title('PhoneBook')

                                scrollbar = Scrollbar(phoneBookView)
                                scrollbar.pack(side = RIGHT, fill = Y)
                                area = Text(phoneBookView, yscrollcommand = scrollbar.set)
                                area.pack()
                                
                                f = open('contacts.dat', 'rb')
                                found = 0
                                try:
                                    while True:
                                        
                                        contacts = {}
                                        contacts = pickle.load(f)
                                        
                                        for each_phone_number in contacts:
                                            if contacts[each_phone_number][1] == email:
                                                found += 1
                                                area.insert(END, '---------------------\n')
                                                area.insert(END, 'Ph. Number: '+each_phone_number+'\n')
                                                area.insert(END, 'Name: '+contacts[each_phone_number][0]+'\n')
                                                area.insert(END, 'Photo Status: '+str(contacts[each_phone_number][2][0])+'\n')

                                        if found == 0:
                                            area.insert(END, "No record found.")
                                except:
                                    f.close()
                                scrollbar.config(command = area.yview)
                                area.config(state = DISABLED)
                                phoneBookView.mainloop()

                            searchNow = Button(searchbyEmailIDWindow, text = "Search", bg = "green", bd = 0,
                                               width = 10, height = 2,
                                            font = ("Arial", 18)
                                            , activebackground = 'green', command = searching,
                                               activeforeground = "White", fg = "White")
                            searchNow.pack()
                            searchNow.place(x = 425, y = 315)
                            
                            searchbyEmailIDWindow.mainloop()

                        var = IntVar()
                        R1 = Radiobutton(searchby, text="Search by Phone Number", variable=var, value=1, command=sbyphno,
                                         bg = 'white', font = ("Arial", 18), activebackground = 'white')
                        R1.pack( anchor = W )
                        R1.place(x = 300, y = 100)

                        R2 = Radiobutton(searchby, text="Search by Name", variable=var, value=2, command=sbyname,
                                         bg = 'white', font = ("Arial", 18), activebackground = 'white')
                        R2.pack( anchor = W )
                        R2.place(x = 300, y = 150)

                        R3 = Radiobutton(searchby, text="Search by Email ID", variable=var, value=3, command=sbyemailid,
                                         bg = 'white', font = ("Arial", 18), activebackground = 'white')
                        R3.pack( anchor = W )
                        R3.place(x = 300, y = 200)

                        searchby.mainloop()
                        

                    addnewcontact = Button(phonebook, text = "Add new contact", bg = "Blue", bd = 0, width = 23, height = 2,
                                       font = ("Arial", 18)
                     , activebackground = 'blue', command = add, activeforeground = "White", fg = "White")
                    addnewcontact.pack()
                    addnewcontact.place(x = 350, y = 105)

                    editcontact = Button(phonebook, text = "Edit a contact", bg = "Blue", bd = 0, width = 23, height = 2,
                                       font = ("Arial", 18)
                     , activebackground = 'blue', command = edit_a_contact, activeforeground = "White", fg = "White")
                    editcontact.pack()
                    editcontact.place(x = 350, y = 230)

                    search = Button(phonebook, text = "Search a contact", bg = "Blue", bd = 0, width = 23, height = 2,
                                       font = ("Arial", 18)
                     , activebackground = 'blue', command = searchC, activeforeground = "White", fg = "White")
                    search.pack()
                    search.place(x = 350, y = 355)

                    phonebook.mainloop()
                    
                else:
                    tkMessageBox.showwarning("Alert", "Wrong Password!!")
            else:
                tkMessageBox.showinfo("Alert", "This is not the registered ID.")

    except:
        f.close()


def signup():
    f = open('account.dat', 'rb')

    try:
        while True:
            d = {}
            d = pickle.load(f)
            z = d
            
            if z == {}:
                f.close()
                root.iconify()
                signupWin = Toplevel()
                signupWin.resizable(height = 0, width = 0)
                signupWin.title("SignUp Window")

                img = ImageTk.PhotoImage(Image.open('Signup.png'))
                panel = Label(signupWin, image = img)
                panel.pack(fill = 'both', expand = True)

                loginId = ttk.Entry(signupWin, width = 40)
                loginId.pack()
                loginId.place(x = 450, y = 120)

                Pass = ttk.Entry(signupWin, width = 40, show = 'x')
                Pass.pack()
                Pass.place(x = 450, y = 170)

                confirmPass = ttk.Entry(signupWin, width = 30, show = 'x')
                confirmPass.pack()
                confirmPass.place(x = 550, y = 225)

                def confirmsignup():
                    f = open('account.dat', 'rb')
                    fw = open('temp.dat', 'wb')

                    try:
                        while True:
                            D = {}
                            D = pickle.load(f)

                            if Pass.get() == confirmPass.get():
                                D.update({loginId.get():Pass.get()})
                                pickle.dump(D, fw)
                                tkMessageBox.showinfo("Alert", "Account created!!")
                                signupWin.destroy()

                            else:
                                tkMessageBox.showwarning("Alert", "Passwords did not matched.")
                                pickle.dump(D, fw)
                    except:
                        f.close()
                    fw.close()
                    os.remove('account.dat')
                    os.rename('temp.dat', 'account.dat')

                confirmSignUp = Button(signupWin, text = "Sign me up", bg = "Blue", bd = 0, width = 9, height = 1,
                                       font = ("Arial", 18)
                     , activebackground = 'blue', command = confirmsignup, activeforeground = "White", fg = "White")
                confirmSignUp.pack()
                confirmSignUp.place(x = 430, y = 315)

                signupWin.mainloop()
            else:
                tkMessageBox.showinfo("Alert", "One account already exists.")
    except:
        f.close()


def delete():

    f = open('account.dat', 'rb')

    try:
        while True:
            d = {}
            d = pickle.load(f)

            if d <> {}:
                f.close()
                root.iconify()
                delWin = Toplevel()
                delWin.resizable(height = 0, width = 0)
                delWin.title("Deletion Window")

                img = ImageTk.PhotoImage(Image.open('delete.png'))
                panel = Label(delWin, image = img)
                panel.pack(fill = 'both', expand = True)
                
                loginId = ttk.Entry(delWin, width = 40)
                loginId.pack()
                loginId.place(x = 450, y = 120)

                Pass = ttk.Entry(delWin, width = 40, show = 'x')
                Pass.pack()
                Pass.place(x = 450, y = 170)

                confirmPass = ttk.Entry(delWin, width = 30, show = 'x')
                confirmPass.pack()
                confirmPass.place(x = 550, y = 225)

                def confirmdeletion():

                    if d.has_key(loginId.get()):
                        if Pass.get() == confirmPass.get():
                            if d[loginId.get()] == Pass.get():
                                if tkMessageBox.askyesno("Alert", "You are about to delete your account. This will also delete your whole phonebook data. Are you sure you want to delete?"):

                                    f = open('contacts.dat', 'rb')

                                    try:
                                        while True:
                                            d1 = {}
                                            d1 = pickle.load(f)

                                            for i in d1:
                                                data_of_contact = d1[i]
                                                user_chose_a_photo = data_of_contact[2][0]
                                                if user_chose_a_photo:
                                                    photoName = data_of_contact[2][1]
                                                    os.remove("%imgs\\"+photoName)
                                    except:
                                        f.close()
                                    
                                    os.remove('account.dat')
                                    os.remove('remember_me.dat')
                                    f = open('account.dat', 'wb')
                                    f1 = open('contacts.dat', 'wb')
                                    f2 = open('remember_me.dat', 'wb')
                                    pickle.dump({}, f1)
                                    pickle.dump({}, f)
                                    pickle.dump([False,], f2)
                                    f.close()
                                    f1.close()
                                    f2.close()
                                    tkMessageBox.showinfo("Alert", "Deleted!!")
                                    delWin.destroy()

                                else:
                                    delWin.destroy()
                            else:
                                tkMessageBox.showwarning("Alert", "Wrong Password!!")
                        else:
                            tkMessageBox.showwarning("Alert", "Passwords did not matched.")
                    else:
                        tkMessageBox.showinfo("Alert", "This is not the registered ID.")

                delButton = Button(delWin, text = "Delete", bg = "Red", bd = 0, width = 8, height = 1, font = ("Arial", 18)
                                 , activebackground = 'Red', command = confirmdeletion)
                delButton.pack()
                delButton.place(x = 430, y = 315)
                
                delWin.mainloop()

            else:
                tkMessageBox.showinfo("Alert", "No account to delete.")
    except:
        f.close()

loginButton = Button(root, text = "Login", bg = "green", bd = 0, width = 4, height = 1, font = ("Arial", 15)
                     , activebackground = 'green', command = login)
loginButton.pack()
loginButton.place(x = 325, y = 290)

signupButton = Button(root, text = "Sign Up", bg = "dark green", bd = 0, width = 6, height = 1, font = ("Arial", 15)
                     , activebackground = 'dark green', command = signup)
signupButton.pack()
signupButton.place(x = 463, y = 290)

delButton = Button(root, text = "Delete A/C", bg = "Red", bd = 0, width = 8, height = 1, font = ("Arial", 11)
                     , activebackground = 'Red', command = delete)
delButton.pack()
delButton.place(x = 613, y = 290)

def callback(event):
    webbrowser.open('http://www.facebook.com/appsandgames24by7/')

fblike = Label(root, text = "Like us on facebook", fg = 'blue', cursor = 'hand2', bg = 'white',
               font = ('Arial', 18))
fblike.pack()
fblike.place(x = 400, y = 380)
fblike.bind('<Button-1>', callback)


root.mainloop()
