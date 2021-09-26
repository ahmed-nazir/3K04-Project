"""
Class used for file I/O
@param none
"""


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
    """
    def writeText(self,text):

    def readText(self):
    """
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
