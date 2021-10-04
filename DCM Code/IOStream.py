"""
Class used for file I/O
"""
import json
import os

class FileIO:
    # Variable Declaration
    # Constants
    # Private Variables
    __fileName = ""
    __mode = ''
    # Public Variables
    """
        Object Constructor
        @param self
        @param fileName string: The name of the file for file I/O
        @param mode char: Specifies if the file is in read(r) or write(w) mode
    """

    def __init__(self, fileName, mode):
        self.__fileName = fileName
        self.__mode = mode
    
    def writeText(self,text):
        if os.path.isfile(self.__fileName):
            #print("The File exists")
            if self.getlength() < 10:
                with open(self.__fileName,"a")as f:
                    f.write(json.dumps(text)+'\n')
            else:
                print("maximum users reached")
        else:
            with open(self.__fileName,"w") as f :
                f.write(json.dumps(text)+'\n')
            

    def readText(self):
        lists=[]
        with open(self.__filName,"r") as f:
            for items in f:
                userdict=json.loads(items)
                lists.append(userdict)
        return(lists)
    
    # Setter functions
    def setMode(self, mode):
        self.__mode = mode

    def setFileName(self, fileName):
        self.__fileName = fileName

    # Getter functions
    def getMode(self):
        return self.__mode

    def getFileName(self):
        return self.__fileName
    
    def getlength(self):
        lists=[]
        with open(self.__filName,"r") as f:
            for items in f:
                userdict=json.loads(items)
                lists.append(userdict)
            return len(lists)
