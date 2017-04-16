import shutil, pickle, os
import tkFileDialog as tfd

def changePhoto(phno):
    f = open('contacts.dat', 'rb')
    parent = {}
    try:
        while True:
            d = {}
            d = pickle.load(f)
            parent = d
            data = d[phno]
            photoName = data[2][1]
    except EOFError:
        f.close()

    try:
        f = tfd.askopenfile()
        s = f.name
        f.close()
        os.remove("%imgs\\"+photoName)
        extension = ''

        reverse = s[-1:-len(s)-1:-1]

        for i in reverse:
            if i<>"/":
                extension+=i
            else:
                break

        name_of_the_photo = extension[-1:-len(extension)-1:-1]

        shutil.copyfile(s, '%imgs//'+extension[-1:-len(extension)-1:-1])
        
        fw = open('temp.dat', 'wb')
        parent[phno][2][1] = name_of_the_photo
        pickle.dump(parent, fw)
        fw.close()
        os.remove('contacts.dat')
        os.rename('temp.dat', 'contacts.dat')
        

    except:
        pass
