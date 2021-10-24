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

    def __init__(self, fileName):
        self.__fileName = fileName
    
    def writeText(self,text):                              
        if os.path.isfile(self.__fileName):
            with open(self.__fileName,"r")as f:
                data = self.readText()
                if not data:
                    data=text
                try:
                    data.update(text)
                except Exception:
                    pass
            with open(self.__fileName,"w")as f:
                f.write(json.dumps(data))
        else:
            with open(self.__fileName,"w") as f :
                f.write(json.dumps(text))
            

    def readText(self):                                    
        try:
            with open(self.__fileName,"r") as f:
                data=json.load(f)
            return data
        except:
            return None
    

    # Getter functions
    def getFileName(self):                                
        return self.__fileName
    
    def getlength(self):                                  
        data = self.readText()
        return len(data)
