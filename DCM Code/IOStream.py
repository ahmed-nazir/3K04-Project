"""
Class used for file I/O
"""
import json
import os

class FileIO:
    """Class used for storing, writing, and reading files
    """
    # Variable Declaration
    # Constants
    # Private Variables
    __fileName = ""



    def __init__(self, fileName):
        """Object Contructor

        Args:
            fileName (string): name of the file to be stored
        """
        self.__fileName = fileName
    
    def writeText(self,text):
        """Check if file exists first and creates one if it doesn’t. 
        Write’s dictionary into the assigned json file.

        Args:
            text (dictionary): dictiory to be added to dictionary
        """
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
        """Read the json file and return the data in the format of dictionary

        Returns:
            [dictionary]: returns dictionary values
        """
        try:
            with open(self.__fileName,"r") as f:
                data=json.load(f)
            return data
        except:
            return None
    

    # Getter functions
    def getFileName(self):
        """Gets the current file name

        Returns:
            [string]: returns the file name
        """
        return self.__fileName
    
    def getlength(self):
        """Gets the length of the dictionary 

        Returns:
            [int]: length of the dictionary
        """
        data = self.readText()
        return len(data)
