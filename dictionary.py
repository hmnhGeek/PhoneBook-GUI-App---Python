import pickle
parent = {}
def returnDictionary(fileName, mode = 'rb'):

    f = open(fileName, mode)

    try:
        while True:
            d = {}
            d = pickle.load(f)
            parent = d

    except EOFError:
        f.close()

    return parent

