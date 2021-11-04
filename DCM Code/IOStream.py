"""
Class used for file I/O
"""
import json
import os
import serial

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
class SerialComm:
    port = None
    baudrate = 0
    bytesize = 0
    parity = ''
    stopbits = 0
    timeout = None
    xonxoff = 0
    rtscts = 0
    """ Object constructor
    """
    def __init__(self):
        self.baudrate=9600
        self.bytesize = 8
        self.parity = 'N'
        self.stopbits = 1
        self.timeout = None
        self.xonxoff = 0
        self.rtscts = 0


    """ Set the current port used for Serial Communication
    """
    def setPort(self,port):
        if(port[0:3]=="COM"):
            self.port=port


    """ Returns a list of all available serial ports in use
    """
    def getSerialPorts(self):
        ports = []
        result = []
        for i in range(256):
            ports.append('COM'+str(i))
        for port in ports:
            try:
                s = serial.Serial(port)
                s.close()
                result.append(port)
            except (OSError, serial.SerialException):
                pass
        return result
    """Attempts to write to serial communication ports stored in port
    """
    def serialWrite(self,data):
        ser = serial.Serial(self.port, self.baudrate, self.bytesize, self.parity, self.stopbits, self.timeout,
                            self.xonxoff, self.rtscts)
        try:
            ser.open()
            if isinstance(data,str):
                dataList = list(data)
                for item in dataList:
                    ser.write(ord(item))
            elif isinstance(data,int):
                ser.write(data)
            ser.close()
        except Exception:
            pass

    """Attempts to read from serial communication ports stored in port
    """
    def serialRead(self):

        ser = serial.Serial(self.port, self.baudrate,self.bytesize, self.parity, self.stopbits, self.timeout, self.xonxoff,self.rtscts)
        try:
            ser.open()
            val =ser.readline()
            ser.close()
            return val
        except Exception:
            pass
