import sys
from glob import glob
from langdetect import detect
import re

class Cesar:
    def __init__(self, fileAlfa, master):
        self.__alfa = self.getAlfa(fileAlfa)
        self.__master = bool(master) #Boolean indicate the master mode

    def readFile(self, fileName):
        with open(fileName, "r+") as f:
            fileString = f.read()
            f.close
        return fileString
    
    def save_file(self, msg, id_):
        with open('./results/msgCesar_'+str(id_)+'.txt', 'w') as f:
            f.write(msg)
            f.close
    
    def getAlfa(self, fileAlfa):
        alfa = self.readFile(fileAlfa).rstrip()
        return alfa
    
    def newChar(self, ch, alfaLen, key):
        index = (self.__alfa.index(ch) - key) % alfaLen
        return self.__alfa[index]

    def tryAnalysis(self, fileName):
        alfaLen = len(self.__alfa)
        cifra = self.readFile(fileName)
        msg = ""
        for i in range(1, alfaLen+1):
            for c in cifra:
                if (c not in self.__alfa):
                    msg = msg + c 
                else:
                    msg = msg + self.newChar(c, alfaLen, i)
            self.save_file(msg, i)
            msg = ""
        if self.__master:
            keys = []
            languages = ["pt"]#, "en", "es", "fr", "ru", "it"]
            files = glob("./results/*.txt")
            for file_ in files:
                textString = self.readFile(file_)
                lan = detect(textString)
                if lan in languages:
                    keys.append(re.sub('[^0-9]', '', file_))
            print("possible keys: ")
            print(keys)
        print("Finish!")

def main():
    try:
        fileAlfa = sys.argv[1]
        fileCifra = sys.argv[2]
    except:
        print("You must provide the alphabet and ciphertext")
    
    masterMode = input("Put the program mode: 0 - Normal Mode | 1 - Master Mode \n")

    cesar = Cesar(fileAlfa, int(masterMode)) 
    cesar.tryAnalysis(fileCifra)

if __name__ == '__main__':
    main()