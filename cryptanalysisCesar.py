import sys
class Cesar:
    def __init__(self, fileAlfa):
        self.__alfa = self.getAlfa(fileAlfa)
    
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
                if (c not in self.__alfa) and (c is not "\n"):
                    msg = msg + c 
                elif c == "\n":
                    msg = msg+"\n"
                else:
                    msg = msg + self.newChar(c, alfaLen, i)
            self.save_file(msg, i)
            msg = ""
        print("Finish!")

def main():
    fileAlfa = sys.argv[1]
    fileCifra = sys.argv[2]
    cesar = Cesar(fileAlfa) 
    cesar.tryAnalysis(fileCifra)

if __name__ == '__main__':
    main()