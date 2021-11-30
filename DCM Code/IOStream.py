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

    def writeText(self, text):
        """Check if file exists first and creates one if it doesn’t. 
        Write’s dictionary into the assigned json file.

        Args:
            text (dictionary): dictionary to be added to dictionary
        """
        if os.path.isfile(self.__fileName):
            with open(self.__fileName, "r") as f:
                data = self.readText()
                if not data:
                    data = text
                try:
                    data.update(text)
                except Exception:
                    pass
            with open(self.__fileName, "w") as f:
                f.write(json.dumps(data))
        else:
            with open(self.__fileName, "w") as f:
                f.write(json.dumps(text))

    def readText(self):
        """Read the json file and return the data in the format of dictionary

        Returns:
            [dictionary]: returns dictionary values
        """
        try:
            with open(self.__fileName, "r") as f:
                data = json.load(f)
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
    __port = None
    __baudrate = 0
    __bytesize = 0
    __parity = serial.PARITY_ODD
    __stopbits = 0
    __timeout = 1
    __xonxoff = 0
    __rtscts = 0
    """ Object constructor
    """

    def __init__(self):
        super().__init__()
        self.__baudrate = 115200
        self.__bytesize = 8
        self.__parity = serial.PARITY_ODD
        self.__stopbits = serial.STOPBITS_ONE
        self.__timeout = 0
        self.__xonxoff = 0
        self.__rtscts = 0
        self.__ser = serial.Serial(self.__port, self.__baudrate, self.__bytesize, self.__parity, self.__stopbits, self.__timeout,
                                   self.__xonxoff, self.__rtscts)

    """ Set the current port used for Serial Communication
    """

    def setPort(self, port):
        if (port[0:3] == "COM"):
            self.__port = port
            self.__ser = serial.Serial(self.__port, self.__baudrate, self.__bytesize, self.__parity, self.__stopbits, self.__timeout,
                                       self.__xonxoff, self.__rtscts)

    """ Returns a list of all available serial ports in use
    """

    def getSerialPorts(self):
        ports = []
        result = []
        for i in range(16):
            ports.append('COM' + str(i))
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

    def serialWrite(self, data):
        try:
            try:
                if (type(data) == str):
                    self.__ser.write(data.encode())
                else:
                    self.__ser.write(data)
            except Exception:
                self.__ser.close()
        except Exception:
            pass

    """ Returns the parity bit of a given bytestring
    """
    def getParityBit(self, data):
        val = []
        if (type(data) == bytes):
            val = "{:08b}".format(int(data.hex(), 16))
        else:
            return b'\x00'
        sum = 0
        for item in val:
            if (item == '1'):
                sum += 1
        if (sum % 2 == 0):
            return b'\x01'
        return b'\x00'

    """Returns the current value stored in port
        
    """

    def getCurrentPort(self):
        return self.__port

    """Attempts to read from serial communication ports stored in port
        """

    def serialRead(self):
        try:
            val = self.__ser.read(16)
            return val
        except Exception:
            pass
