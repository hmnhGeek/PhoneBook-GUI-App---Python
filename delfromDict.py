''' Python script file to delete particular records from a dictionary file. '''


# Importing necessary modules...
import os, pickle
import tkMessageBox as tkM

class delfromDict(object):

    def __init__(self, source_file):

        ''' Initialiser for the module. '''

        self.file = source_file

    def delete(self, key):

        f = open(self.file, 'rb')
        fw = open('temp.dat', 'wb')

        try:
            while True:
                d = {}
                d = pickle.load(f)

                if key in d:
                    if tkM.askyesno("Alert", "Delete this contact?"):
                        data = d[key]
                        os.remove("%imgs//"+data[2][1])
                        del d[key]
                        pickle.dump(d, fw)
                        tkM.showinfo("Alert", "Deleted!!")
                    else:
                        pickle.dump(d, fw)

                else:
                    tkM.showwarning("Alert", "No such phone number in the records.")
                    pickle.dump(d, fw)
        except EOFError:
            f.close()
        fw.close()
        os.remove(self.file)
        os.rename('temp.dat', self.file)


        
                        
                
        
        
