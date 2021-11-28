import struct
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from matplotlib.figure import Figure
from matplotlib import pyplot as plt
import matplotlib.animation as animation
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
NavigationToolbar2Tk)
from IOStream import FileIO, SerialComm
import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random
import serial

from time import sleep
import time
import threading

sc = SerialComm()
write = False
class Run:
    """
    The Run class is used to start the program
    """

    def __init__(self):
        """Object Constructor
        """
        root = tk.Tk()
        # The login window object is created
        cw=ContentWindow(root)
        cw.pack()
        cw.mainloop()

class LoginWindow(tk.Frame):
    """ Extends tk.Frame
        The LoginWindow is a subclass of tk.Frame that stores all the components of the login window. 
    """
    # Variable Declaration
    # Constants
    WIDTH = 30
    HEIGHT = 1
    FONT = ("Arial", 12)
    DEFAULT_USERNAME_TEXT = "Username"
    DEFAULT_PASSWORD_TEXT = "Password"
    DEFAULT_LOGIN_BUTTON_TEXT = "Login"
    DEFAULT_REGISTER_BUTTON_TEXT = "Register"
    PADDING = 10
    BACKGROUND_COLOR = "#FAF9F6"
    FOREGROUND_COLOR = "#C0C0C0"
    PASSWORDFILE = "password.json"

    # Private Variables
    __mainWindow = None
    __usernameField = None
    __passwordField = None
    __loginButton = None
    __registerButton = None
    __password = None
    __username = None
    __buttonFrame = None
    __paddingFrame = None
    # Public Variables


    def __init__(self, mainWindow):
        """Object Constructor

        Args:
            mainWindow (ContentWindow): the higher frame that stores the LoginWindow
        """
        tk.Frame.__init__(self, mainWindow, bg=self.FOREGROUND_COLOR, width=200, height=200, padx=self.PADDING, pady=self.PADDING, relief=tk.RIDGE, borderwidth=3)
        self.__mainWindow = mainWindow
        # Initialize components of frame
        self.__initializeEntryFields()
        self.__initializeButtons()
        # Initialize frame properties
        self.__paddingFrame = Frame(mainWindow,bg=self.BACKGROUND_COLOR,width=300,height=150)
        self.__paddingFrame.pack()

    

    def __initializeEntryFields(self):
        """Initializes entry field for user login window
        """
        self.__usernameField = Entry(self, width=self.WIDTH, font=self.FONT)
        self.__usernameLabel = Label(self, text=self.DEFAULT_USERNAME_TEXT, bg=self.FOREGROUND_COLOR)
        self.__passwordLabel = Label(self, text=self.DEFAULT_PASSWORD_TEXT, bg=self.FOREGROUND_COLOR)
        self.__usernameLabel.pack(pady=self.PADDING/3)
        self.__usernameField.pack(pady=self.PADDING)
        self.__passwordLabel.pack(pady=self.PADDING/3)
        self.__passwordField = Entry(self, width=self.WIDTH, font=self.FONT, show="*")
        self.__passwordField.pack(pady=self.PADDING)

    

    def __initializeButtons(self):
        """Initializes the buttons to login and register a user
        """
        self.__buttonFrame = Frame(self, bg=self.FOREGROUND_COLOR)
        self.__loginButton = Button(self.__buttonFrame, text=self.DEFAULT_LOGIN_BUTTON_TEXT, command=self.checkPass,relief="flat")

        self.__loginButton.grid(row=0, column=0, padx=5, pady=10)

        self.__registerButton = Button(self.__buttonFrame, text=self.DEFAULT_REGISTER_BUTTON_TEXT,command=self.registerUser,relief="flat")
        self.__registerButton.grid(row=0, column=1, padx=5, pady=10)

        self.__buttonFrame.pack()

  

    def getText(self):
        """Gets the user input variables in the login screen and stores in the class username and password fields
        """
        self.__password = self.__passwordField.get()
        self.__username = self.__usernameField.get()
        # Code below is when there is a matching password and key, the program
        # will remove the password screen and add the main program
        # --Note: figure out a way to only remove content pane instead of removing all elements in content pane
    
    def checkPass(self):
        """Checks whether the credentials the user inputted is correct. Calls the higher frame window’s login function if successful. 
        """
        self.getText()
        alt=FileIO(self.PASSWORDFILE)
        f = alt.readText()
        if not(f):
           alt.writeText("")
           f = ""

        if (self.__username == "" or self.__password == ""):
            messagebox.showinfo("Error: No Data Entered","NO DATA ENTERED")
        elif self.__username in f:
            if self.__password==f[self.__username]:
                self.__paddingFrame.pack_forget()
                self.__mainWindow.login()
            else:
                messagebox.askretrycancel("User Validation","Wrong password,try again?")
        else:
            messagebox.showinfo("User Validation","User not registered, Please Register User")

    
    def registerUser(self):
        """Registers a new user and checks whether a user already exists
        """
        alt=FileIO(self.PASSWORDFILE)
        d=alt.getlength()
        f = alt.readText()
        self.getText()
        text={self.__username:self.__password}
        if (self.__username == "" or self.__password == ""):
            messagebox.showinfo("Error: No Data Entered","NO DATA ENTERED")
        elif (self.__username in f):
            messagebox.showinfo("Error: User Already Registered","Try another username")
        elif d==10:
            messagebox.showinfo("User Validation","Maximum number of users reached")
        else:
            alt.writeText(text)
            messagebox.showinfo("User Registerd","User Successfully Registered")
    
    def getUsername(self):
        """Returns the username of the current user

        Returns:
            __username (string): returns the username value
        """
        return self.__username
    
    def clearVal(self):
        """Clears the entry fields in LoginWindow
        """
        self.__usernameField.delete(0,END)
        self.__usernameField.pack()
        self.__passwordField.delete(0,END)
        self.__passwordField.pack()
    
    def setPaddingVisible(self):
        """ Helper function for formatting
        """
        self.__paddingFrame.pack()


class GraphWindow(tk.Frame):
    """ Extends tk.Frame
        The GraphWindow is a subclass of tk.Frame that stores all the components of the graph
    """
    __mainWindow=None
    xdata, ydata, y1data = [], [], []
    fig, ax = plt.subplots()
    def __init__(self, mainWindow):
        """Object Constructor

        Args:
            mainWindow (frame): the higher frame that stores the LoginWindow
        """
        tk.Frame.__init__(self, mainWindow, bg="yellow", width="200", height="200")
        self.__mainWindow = mainWindow
        self.plot()
        #while(True):
         #   self.plot()
    def getValues(self,data):
        t, rand, rand1 = data
        self.xdata.append(t)
        self.ydata.append(rand)
        self.y1data.append(rand1)

        xmin, xmax = self.ax.get_xlim()
        if t >= xmax:  # update x-axis
            self.ax.set_xlim(xmin + 1, xmax + 1)
            self.ax.figure.canvas.draw()
        # line.set_data(xdata,ydata)
        self.ax.plot(self.xdata, self.ydata, color="red")
        self.ax.plot(self.xdata, self.y1data, color="blue")

    def plot(self):
        """Draws the graph in the DCM window
        """
        fig = Figure(figsize=(4, 4),dpi=100)
        y = [math.sin(i/10) for i in range(1,200)]
        plot1 = fig.add_subplot(111)
        plot1.plot(y)
        canvas = FigureCanvasTkAgg(fig,master=self)
        canvas.draw()
        canvas.get_tk_widget().pack()

class DCMWindow(tk.Frame):
    """ Extends tk.Frame
        The DCMWindow is a subclass of tk.Frame that stores all the components of the DCM Window. 
    """
    # Constants
    PARAMLABELS = ["Lower Rate Limit","Upper Rate Limit","Atrial Amplitude","Ventricular Amplitude","Atrial Pulsewidth","Ventricular Pulsewidth","Atrial Refractory Period","Ventricular Refractory Period","Atrium Sense","Ventricle Sense","MSR","Recovery Time","Reaction Time","Response Factor","Activity Threshold","AV Delay",""]
    LRL = [30,35,40,45,50]
    URL = []
    ATRAMP = ["Off"]
    VENTAMP = ["Off"]
    ATRWIDTH = []
    VENTWIDTH = []
    ATRREFRAC = []
    VENTREFRAC = []
    ASENSE=[0]
    VSENSE=[0]
    MSR=[]
    RECOVERYTIME=[]
    REACTIONTIME=[]
    RESPONSEFACTOR=[]
    ACTIVITYTHRESHOLD=["V-Low","Low","Med-Low","Med","Med-High","High","V-High"]
    AVDELAY=[]
    PROGRAMABLEPARAMETERS = [LRL,URL,ATRAMP,VENTAMP,ATRWIDTH,VENTWIDTH,ATRREFRAC,VENTREFRAC,ASENSE,VSENSE,MSR,RECOVERYTIME,REACTIONTIME,RESPONSEFACTOR,ACTIVITYTHRESHOLD,AVDELAY]
    PARAMETERFILE = "parameters.json"
    TYPELIST = ["8","8","f","f","8","8","16","16","f","f","8","8","8","8","f","16"]
    NUMBEROFPARAMETERS = len(PROGRAMABLEPARAMETERS)
    MODELABELS = ["AOO", "VOO", "AAI", "VVI","AOOR","VOOR","AAIR","VVIR","DOO","DOOR"]
    #The following variable is a placeholder before serial communication is implemented
    BACKGROUND_COLOR = "#FAF9F6"
    SERIALCOMMODE = SerialComm().getSerialPorts()
    ACTIVITYTHRESHOLDDICT = {"V-Low":1.1,"Low":1.3,"Med-Low":1.5,"Med":1.7,"Med-High":1.9,"High":2.1,"V-High":2.3}

    # Private Variables
    __mainWindow = None
    __labelArr=[]
    __entryArr=[]
    __modeList = None
    __currentMode = None
    __currentPort = None
    __saveButton = None
    __comMode = None
    __usernameLabel = None
    __logoutButton = None
    __comButton= None
    __consoleLog = None
    __buttonSend = None
    __username = None
    __showState = ["readonly","readonly","readonly","readonly","readonly","readonly","readonly","readonly"]
    __graphWindowButton = None

    def __init__(self, mainWindow,username):
        """Object Constructor

        Args:
            mainWindow (ContentWindow): the higher frame that stores the DCMWindow
            username (string): stores the username
        """
        tk.Frame.__init__(self,mainWindow,bg=self.BACKGROUND_COLOR,width=1280,height=600)
        self.__username=username
        self.__initalizeConstants()
        self.__mainWindow = mainWindow
        self.__mainWindow.focus_set()
        self.__currentMode=""
        self.__currentPort = StringVar(self)
        self.__initalizeTopFrame(username)
        self.__centerFrame = Frame(self,bg=self.BACKGROUND_COLOR,width=1280,height=550)
        self.__centerFrame.pack()
        #self.__initalizeLeftFrame()

        t1_gw = threading.Thread(target=self.__displayGraph)
        t1_gw.start()
        self.__initalizeRightFrame()
        self.__initalizeBottomFrame()

    def __initalizeTopFrame(self,username):
        """Initializes top frame of the DCM Window

        Args:
            username (string): stores the username
        """
        self.__topFrame = Frame(self, bg=self.BACKGROUND_COLOR, width=1280, height=50)
        self.__usernameLabel = Label(self.__topFrame,text="User: "+username,bg=self.BACKGROUND_COLOR)
        self.__usernameLabel.grid(row=0,column=0,padx=110)
        self.__comMode = ttk.Combobox(self.__topFrame, values= self.SERIALCOMMODE,state = "readonly")
        self.__comMode.grid(row=0,column=1,padx=5)
        self.__comButton = Button(self.__topFrame, text="Connect",bg="red", command=self.checkPort, relief="flat", padx=20)
        self.__comButton.grid(row=0,column=2,padx=5)
        self.__logoutButton = Button(self.__topFrame, text="Logout", command=self.logout, relief="flat", padx=20)
        self.__logoutButton.grid(row=0, column=3,padx=230)
        self.__topFrame.pack()

    #NO LONGER USED DELETE IN FUTURE
    def __initalizeLeftFrame(self):
        """Initializes left frame of the DCM Window
        """
        self.__leftFrame = Frame(self.__centerFrame, bg=self.BACKGROUND_COLOR, width=640, height=550)
        self.__leftFrame.grid(row=0,column=0)
        #t1_gw = threading.Thread(target=self.startGraphWindow)
        #t1_gw.start()
        #self.__graphWindow = GraphWindow(self.__leftFrame)
        #self.__graphWindow.pack()

    def startGraphWindow(self):
        self.__graphWindow = GraphWindow(self.__leftFrame)
        self.__graphWindow.pack()

    def __initalizeRightFrame(self):
        """Initializes right frame of the DCM Window
        """
        self.__rightFrame = Frame(self.__centerFrame, bg=self.BACKGROUND_COLOR, width=640, height=550)
        self.__rightFrame.grid(row=0,column=1)
        topRight = Frame(self.__rightFrame, bg=self.BACKGROUND_COLOR, width=640, height=275)
        bottomRight = Frame(self.__rightFrame, bg=self.BACKGROUND_COLOR, width=640, height=275)
        topRight.pack()
        bottomRight.pack()
        self.__saveButton = Button(topRight, text="Select Mode", command=self.__modeSelect, relief="flat", padx=20)
        self.__saveButton.grid(row=0, column=1, padx=20, pady=20)
        #self.__modeList = OptionMenu(topRight, self.__currentMode, *self.MODELABELS)
        self.__modeList = ttk.Combobox(topRight,values = self.MODELABELS,state="readonly")
        self.__modeList.grid(row=0, column=0, padx=20, pady=20)
        self.__initalizeParameterList(bottomRight)
    def __initalizeBottomFrame(self):
        """Initializes bottom frame of the DCM Window
        """
        self.__bottomFrame = Frame(self, bg=self.BACKGROUND_COLOR, width=1280, height=10)
        self.__bottomFrame.pack()
        self.__buttonSend = Button(self.__bottomFrame,text="Send",command=self.__saveParameters,relief="flat", padx=100)
        self.__buttonSend.grid(row=0, column=1, padx=20, pady=20)
        self.__graphWindowButton = Button(self.__bottomFrame,text="Display Graph",command=self.__displayGraph,relief="flat", padx=10)
        self.__graphWindowButton.grid(row=0, column=3, padx=20, pady=20)
        #self.__consoleLog = Text(self.__bottomFrame,width=100,height=5,state="disabled")
        #self.__consoleLog.pack(pady=10)
    def __displayGraph(self):
        random.seed()  # random number test case initialize
        c=0
        while True:
            if not write:
                t = time.time()
                sc.serialWrite(b'\x16\x22\00\x3C\x78\x00\x00\xA0\x40\x00\x00\xA0\x40\x02\x02\xFA\x00\xFA\x00\x00\x00\x80\x40\x00\x00\x80\x40\x64\x02\x0A\x10\xCD\xCC\x8C\x3F\x64\x00')
                elapsed = time.time() - t
                print(elapsed)

                try:

                   # print("YES")
                    val, = struct.unpack('d', sc.serialRead())
                    print(val)
                except Exception:
                    if(c%500000==0):
                        print(c)
                    c+=1
            else:
                sleep(1)
        print("end")
        fig, ax = plt.subplot()
        ax.set_ylim(0, 10)  # initialize maximum value of the axis
        ax.set_xlim(0, 10)
        ani = animation.FuncAnimation(fig, self.run, init_func=self.init, interval=100)  # Interval updating each data point in ms
        plt.show()

    def run(self,data):
        xdata, ydata, y1data = [], [], []
        ax = plt.subplot()
        t, rand, rand1 = data
        xdata.append(t)
        ydata.append(rand)
        y1data.append(rand1)
        while(True):
            print(sc.serialRead())
        xmin, xmax = ax.get_xlim()
        if t >= xmax:  # update x-axis
            ax.set_xlim(xmin + 1, xmax + 1)
            ax.figure.canvas.draw()
        # line.set_data(xdata,ydata)
        ax.plot(xdata, ydata, color="red")
        ax.plot(xdata, y1data, color="blue")
        # return line,
    def init(self):
        ax = plt.subplot()
        line, = ax.plot([], [], lw=2)
        line.set_data([], [])
        return line,
    def __modeSelect(self):
        """Mode selector between different Heart modes (AOO,AAI,VOO,VVI)
        """

        if self.__modeList.get() == "AOO":
            self.__hideParameter(
                ["readonly", "readonly", "readonly", "disabled", "readonly", "disabled", "disabled", "disabled","disabled","disabled", "disabled", "disabled","disabled", "disabled", "disabled", "disabled"])
            self.__currentMode = "AOO"
        elif self.__modeList.get() == "AAI":
            self.__hideParameter(
                ["readonly", "readonly", "readonly", "disabled", "readonly", "disabled", "readonly", "disabled","readonly","disabled", "disabled", "disabled","disabled", "disabled", "disabled", "disabled"])
            self.__currentMode = "AAI"
        elif self.__modeList.get() == "VOO":
            self.__hideParameter(
                ["readonly", "readonly", "disabled", "readonly", "disabled", "readonly", "disabled", "disabled","disabled","disabled", "disabled", "disabled","disabled", "disabled", "disabled", "disabled"])
            self.__currentMode = "VOO"
        elif self.__modeList.get() == "VVI":
            self.__hideParameter(
                ["readonly", "readonly", "disabled", "readonly", "disabled", "readonly", "disabled", "readonly","disabled","readonly", "disabled", "disabled","disabled", "disabled", "disabled", "disabled"])
            self.__currentMode = "VVI"
        elif self.__modeList.get() == "AOOR":
            self.__hideParameter(
                ["readonly", "readonly", "readonly", "disabled", "readonly", "disabled", "disabled", "disabled",
                 "disabled", "disabled", "readonly", "readonly", "readonly", "readonly", "readonly", "disabled"])
            self.__currentMode = "AOOR"
        elif self.__modeList.get() == "AAIR":
            self.__hideParameter(
                ["readonly", "readonly", "readonly", "disabled", "readonly", "disabled", "readonly", "disabled",
                 "readonly", "disabled",  "readonly", "readonly", "readonly", "readonly", "readonly", "disabled"])
            self.__currentMode = "AAIR"
        elif self.__modeList.get() == "VOOR":
            self.__hideParameter(
                ["readonly", "readonly", "disabled", "readonly", "disabled", "readonly", "disabled", "disabled",
                 "disabled", "disabled",  "readonly", "readonly", "readonly", "readonly", "readonly", "disabled"])
            self.__currentMode = "VOOR"
        elif self.__modeList.get() == "DOO":
            self.__hideParameter(
                ["readonly", "readonly", "readonly", "readonly", "readonly", "readonly", "disabled", "disabled",
                 "disabled", "disabled", "disabled", "disabled", "disabled", "disabled", "disabled", "readonly"])
            self.__currentMode = "DOO"
        elif self.__modeList.get() == "DOOR":
            self.__hideParameter(
                ["readonly", "readonly", "readonly", "readonly", "readonly", "readonly", "disabled", "disabled",
                 "disabled", "disabled", "readonly", "readonly", "readonly", "readonly", "readonly", "readonly"])
            self.__currentMode = "DOOR"
    def __hideParameter(self,showState):
        """Changes that status of the drop-down selector for each parameter

        Args:
            showState (array): array of values setting the buttons active or inactive eg. [“readonly”]
        """
        for i in range(len(showState)):
            self.__entryArr[i].config(state = showState[i])

    def __saveParameters(self):
        """Exports the sent parameters to an external json file
        """
        global write
        write=True
        alt = FileIO(self.__username+self.__currentMode+self.PARAMETERFILE)
        f = alt.readText()
        arr = []
        if not(f):
           alt.writeText("")
           f = ""
        for i in range(self.NUMBEROFPARAMETERS):
            alt.writeText({self.PARAMLABELS[i]:""})
        alt.writeText({"Mode":self.__currentMode})
        arr.append((self.MODELABELS.index(self.__currentMode)).to_bytes(1, byteorder='little'))
        for i in range(self.NUMBEROFPARAMETERS):
            try:
                    #print(self.__entryArr[i]["state"])
                    #if (self.__entryArr[i]["state"] == "disabled"):
                     #   raise ValueError()
                    if(self.TYPELIST[i]=="8"):
                        arr.append(int(self.__entryArr[i].get()).to_bytes(1, byteorder='little'))
                    elif(self.TYPELIST[i]=="f"):
                            temparr=(bytearray(struct.pack('f', float(self.__entryArr[i].get()))))
                            for item in temparr:
                                val = int(item)
                                arr.append(val.to_bytes(1, byteorder='little'))
                    else:
                            val = int(self.__entryArr[i].get()).to_bytes(2, byteorder='little')
                            arr.append(val)

            except ValueError:
                if(str(self.__entryArr[i].get()) in self.ACTIVITYTHRESHOLD ):
                    val = self.ACTIVITYTHRESHOLDDICT[str(self.__entryArr[i].get())]
                    temparr = bytearray(struct.pack('f', val))
                    for item in temparr:
                        val = int(item)
                        arr.append(val.to_bytes(1, byteorder='little'))
                else:
                    if (self.TYPELIST[i] == "8"):
                        arr.append(b'\x00')
                    elif (self.TYPELIST[i] == "f"):
                            arr.append(b'\x00')
                            arr.append(b'\x00')
                            arr.append(b'\x00')
                            arr.append(b'\x00')
                    else:
                        arr.append(b'\x00')
                        arr.append(b'\x00')

                if (self.__entryArr[i]["state"] == "readonly"):
                    text = {self.PARAMLABELS[i]:self.__entryArr[i].get()}
                    alt.writeText(text)

        print(arr)
        #sc = SerialComm()
        val=b'\x16\x55'
        for item in arr:
            val = val+item
        #sc.setPort(str(self.__currentPort))
        #sc.serialWrite(val)
        print(self.__currentPort)
        print(val)
        #t1_sc = threading.Thread(target=self.serialCommWrite, args=(val,    ))
        #t1_sc.start()
        self.serialCommWrite(val)

    def serialCommWrite(self, val):
        global write
        print(type(val))
        #sc.setPort(str(self.__currentPort))
        print(sc.port)
        sc.serialWrite(val)
        print(val)
        write=False

    def resetMode(self):
        """Reset the bradycardia state back to VOO
        """
        self.__modeList.set("VOO")
        self.__hideParameter(["readonly", "readonly", "disabled", "readonly", "disabled", "readonly", "disabled", "disabled"])
        self.__currentMode="VOO"
        for item in self.__entryArr:
            item.set("")


    def checkPort(self):
        """Checks which port is selected
        """
        self.__currentPort=self.__comMode.get()
        t2_sc = threading.Thread(target=self.runPort)
        t2_sc.daemon=True
        t2_sc.start()
        #t2_sc.join(1)
    def runPort(self):
        self.__comMode["values"] = SerialComm().getSerialPorts()

    def logout(self):
        """Logs out of the main interface
        """
        self.__mainWindow.logout()


    def setUsername(self,username):
        """Shows the username of the current user on the top left of the DCM window

        Args:
            username (string): stores the username
        """
        self.__usernameLabel.config(text="User: " +username)
        self.__username = username
    
    def __initalizeParameterList(self,higherFrame):
        """ Creates a grid of labels and drop down menus for parameter value inputs

        Args:
            higherFrame (tk.Frame): The higher level frame the components are stored in
        """
        #Initialzing all the parameter boxes
        for i in range(0,self.NUMBEROFPARAMETERS,4):
            for j in range(4):
                label=Label(higherFrame,text=self.PARAMLABELS[i+j],bg=self.BACKGROUND_COLOR)
                entry = ttk.Combobox(higherFrame,values=self.PROGRAMABLEPARAMETERS[i+j],state="disabled")
                self.__labelArr.append(label)
                label.grid(row=i,column=j,padx=20,pady=10)
                self.__entryArr.append(entry)
                entry.grid(row=i+1,column=j,padx=20,pady=10)
    def __initalizeConstants(self):
        """ Helper function to create values for different parameter settings
        """
        for i in range(40):
            self.LRL.append(51 + i)
        for i in range(17):
            self.LRL.append(95 + 5 * i)

        for i in range(26):
            self.URL.append(50 + i * 5)
            self.MSR.append(50 + i*5)

        for i in range(50):
            self.ATRAMP.append(round(0.1 + 0.1 * i, 1))
            self.VENTAMP.append(round(0.1 + 0.1 * i, 1))
            self.ASENSE.append(round(0.1 + 0.1 * i, 1))
            self.VSENSE.append(round(0.1 + 0.1 * i, 1))
        for i in range(30):
            self.ATRWIDTH.append(1 + i)
            self.VENTWIDTH.append(1 + i)
        for i in range(36):
            self.ATRREFRAC.append(150 + 10 * i)
            self.VENTREFRAC.append(150 + 10 * i)
        for i in range(2,17,1):
            self.RECOVERYTIME.append(i)
        for i in range(10,51,10):
            self.REACTIONTIME.append(i)
        for i in range(1,17):
            self.RESPONSEFACTOR.append(i)
        for i in range(70,301,10):
            self.AVDELAY.append(i)
class ContentWindow(tk.Frame):
    """ Extends tk.Frame
        The ContentWindow is a subclass of tk.Frame that stores all the components of the Content Window.
        The ContentWindow is used to manage the interactions of the other frames in the DCM.
    """

    # Private Variables
    __loginWindow = None
    __parent = None
    __DCM = None

    # Public Variable
    username = ""


    def __init__(self,parent):
        """Object Constructor

        Args: parent (tk.Tk): The top level frame holding the ContentWindow. Currently, this should be the
        tk.Tk() as ContentWindow is a top level window manager
        """
        tk.Frame.__init__(self,parent)
        self.__parent=parent
        parent.title("DCM")
        parent.geometry("1200x600")
        parent.resizable(False,False)
        parent.config(bg='#FAF9F6')
        self.__loginWindow = LoginWindow(self)
        self.__DCM = DCMWindow(self,self.username)
        self.__loginWindow.pack()

    def login(self):
        """ The method disables the login window screen and enables the DCM interface, along with formatting
        """
        self.__loginWindow.pack_forget()
        self.username = self.__loginWindow.getUsername()
        self.__DCM.setUsername(self.username)
        self.__DCM.resetMode()
        self.__DCM.pack()
    def logout(self):
        """ The method disables the DCM interface and enables the login window screen, along with formatting
        """
        self.__DCM.pack_forget()
        #self.__loginWindow.clearVal()
        self.__loginWindow.setPaddingVisible()
        self.__loginWindow.pack()

# Main script
if __name__ == "__main__":
    run = Run()
    print(sc.getSerialPorts())
    sc.setPort(sc.getSerialPorts()[0])

    #sc.serialWrite(b'\x16\x55\00\x3C\x78\x00\x00\xA0\x40\x00\x00\xA0\x40\x02\x02\xFA\x00\xFA\x00\x00\x00\x80\x40\x00\x00\x80\x40\x64\x02\x0A\x10\xCD\xCC\x8C\x3F\x64\x00')
    while(True):
        sc.serialWrite(b'\x16\x22\00\x3C\x78\x00\x00\xA0\x40\x00\x00\xA0\x40\x02\x02\xFA\x00\xFA\x00\x00\x00\x80\x40\x00\x00\x80\x40\x64\x02\x0A\x10\xCD\xCC\x8C\x3F\x64\x00')
        try:
            val,=struct.unpack('d',sc.serialRead())
            print(val)
        except Exception:
            print("None")


    #print(b'\x16\x22\00\x3C\x78\x00\x00\xA0\x40\x00\x00\xA0\x40\x02\x02\xFA\x00\xFA\x00\x00\x00\x80\x40\x00\x00\x80\x40\x64\x02\x0A\x10\xCD\xCC\x8C\x3F\x64\x00')