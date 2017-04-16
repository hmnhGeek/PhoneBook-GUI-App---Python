
''' Script to change username and password. '''

# Importing necessary modules...

import os, pickle
from tkMessageBox import *



class changeDetails(object):

    def __init__(self, username, password, file_handle):

        ''' Initialising proper variables. '''
        
        self.u = username
        self.p = password
        self.f = file_handle

    def check(self):
        f = open(self.f, 'rb')

        try:
            while True:
                d = {}
                d = pickle.load(f)

                if self.u in d:
                    if d[self.u] == self.p:
                        return 1
                    else:
                        return 0
                else:
                    return 0
        except EOFError:
            f.close()
    
    def dumpNow(self):

        f = open('temp.dat', 'wb') # Opening a temporary file.

        pickle.dump({self.u:self.p}, f) # Dump a new dictionary file in it.

        f.close()

        os.remove(self.f) # Remove old file...
        os.rename('temp.dat', self.f) # Rename the temp file with the original file name.


    def changeUsername(self, new_username):

        if self.check():
            self.u = new_username
            self.dumpNow() # Call dumpNow() to dump updated username.
        else:
            showwarning("Alert", "Something is wrong!!")


    def changePassword(self, new_password):

        if self.check():
            self.p = new_password
            self.dumpNow() # Call dumpNow() to dump updated username.

        else:
            showwarning("Alert", "Something is wrong!!")


    def changeBoth(self, new_username, new_password):

        if self.check():
            self.changeUsername(new_username)
            self.changePassword(new_password)
            self.dumpNow() # Call dumpNow() to dump updated username.
        else:
            showwarning("Alert", "Something is wrong!!")

