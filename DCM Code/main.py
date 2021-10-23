import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
NavigationToolbar2Tk)
from IOStream import FileIO
import math

"""
    The Run class is used to start the program
"""


class Run:
    """
        Object Constructor
        @param self
    """

    def __init__(self):
        root = tk.Tk()
        # The login window object is created
        cw=ContentWindow(root)
        cw.pack()
        cw.mainloop()

"""
    The LoginWindow class is the the inital interface in viewing the program
    Extends tk.Frame  
"""


class LoginWindow(tk.Frame):
    # Variable Declaration
    # Constants
    WIDTH = 30
    HEIGHT = 1
    FONT = ("Arial", 12)
    DEFAULT_USERNAME_TEXT = "Username"
    DEFAULT_PASSWORD_TEXT = "Password"
    DEFAULT_login_BUTTON_TEXT = "Login"
    DEFAULT_REGISTER_BUTTON_TEXT = "Register"
    PADDING = 10
    BACKGROUND_COLOR = "#FAF9F6"
    FOREGROUND_COLOR = "#C0C0C0"
    PASSWORDFILE = "DCM Code\password.json"

    # Private Variables
    __root = None
    __mainWindow = None
    __usernameField = None
    __passwordField = None
    __loginButton = None
    __registerButton = None
    __password = None
    __username = None
    __contentPane = None
    __buttonFrame = None
    __paddingFrame = None
    # Public Variables

    """
        Object Constructor
        @param self
    """

    def __init__(self, mainWindow):
        tk.Frame.__init__(self, mainWindow, bg=self.FOREGROUND_COLOR, width=200, height=200, padx=self.PADDING, pady=self.PADDING, relief=tk.RIDGE, borderwidth=3)
        self.__mainWindow = mainWindow
        self.__root = mainWindow
        # Initialize components of frame
        self.__initializeEntryFields()
        self.__initializeButtons()
        # Initialize frame properties
        self.__root.config(bg=self.BACKGROUND_COLOR)
        self.__paddingFrame = Frame(mainWindow,bg=self.BACKGROUND_COLOR,width=150,height=150)
        self.__paddingFrame.pack()

    """
        Initializes the text fields and adds formatting to them
        @param self
    """

    def __initializeEntryFields(self):
    
        self.__usernameField = Entry(self, width=self.WIDTH, font=self.FONT)
        self.__usernameLabel = Label(self, text=self.DEFAULT_USERNAME_TEXT, bg=self.FOREGROUND_COLOR)
        self.__passwordLabel = Label(self, text=self.DEFAULT_PASSWORD_TEXT, bg=self.FOREGROUND_COLOR)
        self.__usernameLabel.pack(pady=self.PADDING/3)
        self.__usernameField.pack(pady=self.PADDING)
        self.__passwordLabel.pack(pady=self.PADDING/3)
        self.__passwordField = Entry(self, width=self.WIDTH, font=self.FONT, show="*")
        self.__passwordField.pack(pady=self.PADDING)

    """
       Initializes the buttons and adds formatting to them
       @param self
    """

    def __initializeButtons(self):
        self.__buttonFrame = Frame(self, bg=self.FOREGROUND_COLOR)
        self.__loginButton = Button(self.__buttonFrame, text=self.DEFAULT_login_BUTTON_TEXT, command=self.CheckPass,relief="flat")

        self.__loginButton.grid(row=0, column=0, padx=5, pady=10)

        self.__registerButton = Button(self.__buttonFrame, text=self.DEFAULT_REGISTER_BUTTON_TEXT,command=self.registerUser,relief="flat")
        self.__registerButton.grid(row=0, column=1, padx=5, pady=10)

        self.__buttonFrame.pack()

    """
        Function is called when the login button is pressed, validates the password to the stored file and 
        will enter the DCM window if successful
        @param self
    """

    def getText(self):
        self.__password = self.__passwordField.get()
        self.__username = self.__usernameField.get()
        # Code below is when there is a matching password and key, the program
        # will remove the password screen and add the main program
        # --Note: figure out a way to only remove content pane instead of removing all elements in content pane
    
    def CheckPass(self):

        self.getText()
        alt=FileIO(self.PASSWORDFILE)
        f=alt.readText()
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

    """
        Function opens a frame to add new credentials if applicable
        @param self
    """
    def registerUser(self):
        """Test a"""
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
        return self.__username
    def clearVal(self):
        self.__usernameField.delete(0,END)
        self.__usernameField.pack()
        self.__passwordField.delete(0,END)
        self.__passwordField.pack()
    def setPaddingVisible(self):
        self.__paddingFrame.pack()


class GraphWindow(tk.Frame):
    __mainWindow=None
    def __init__(self, mainWindow):
        tk.Frame.__init__(self, mainWindow, bg="yellow", width="640", height="550")
        self.__mainWindow = mainWindow
        self.plot()
    def plot(self):
            fig = Figure(figsize=(4, 4),dpi=100)
            y = [math.sin(i/10) for i in range(1,200)]
            plot1 = fig.add_subplot(111)
            plot1.plot(y)
            canvas = FigureCanvasTkAgg(fig,master=self)
            canvas.draw()
            canvas.get_tk_widget().pack()

class DCMWindow(tk.Frame):
    # Constants
    PARAMLABELS = ["Lower Rate Limit","Upper Rate Limit","Atrial Amplitude","Ventricular Amplitude","Atrial Pulsewidth","Ventricular Pulsewidth","Atrial Refractory Period","Ventricular Refractory Period"]
    LRL = [30,35,40,45,50]
    URL = []
    ATRAMP = ["Off"]
    VENTAMP = ["Off"]
    ATRWIDTH = [0.05]
    VENTWIDTH = [0.05]
    ATRREFRAC = []
    VENTREFRAC = []
    # Sets the values of each parameter
    for i in range(40):
        LRL.append(51+i)
    for i in range(17):
        LRL.append(95+5*i)

    for i in range(26):
        URL.append(50 + i*5)

    for i in range(28):
        ATRAMP.append(round(0.5 + 0.1*i,1))
        VENTAMP.append(round(0.5 + 0.1*i,1))
    for i in range(8):
        ATRAMP.append(round(3.5 + 0.5*i,1))
        VENTAMP.append(round(3.5 + 0.5*i,1))
    
    for i in range(19):
        ATRWIDTH.append(round(0.1 + i*0.1,1))
        VENTWIDTH.append(round(0.1 + i*0.1,1))

    for i in range(36):
        ATRREFRAC.append(150 + 10*i)
        VENTREFRAC.append(150 + 10*i)


    PROGRAMABLEPARAMETERS = [LRL,URL,ATRAMP,VENTAMP,ATRWIDTH,VENTWIDTH,ATRREFRAC,VENTREFRAC]

    MODELABELS = ["AOO", "VOO", "AAI", "VVI"]
    #The following variable is a placeholder before serial communication is implemented
    BACKGROUND_COLOR = "#FAF9F6"
    SERIALCOMMODE = ["COM8","COM9"]
    # Padding is in PX
    PADDING = 20
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
    showState = ["readonly","readonly","readonly","readonly","readonly","readonly","readonly","readonly"]
    """
        Constructor
        @param mainWindow
    """

    def __init__(self, mainWindow,username):
        tk.Frame.__init__(self,mainWindow,bg=self.BACKGROUND_COLOR,width=1280,height=600)
        self.__mainWindow = mainWindow
        self.__mainWindow.focus_set()
        self.__currentMode=StringVar(self)
        self.__currentPort = StringVar(self)
        self.initalizeTopFrame(username)
        self.__centerFrame = Frame(self,bg=self.BACKGROUND_COLOR,width=1280,height=550)
        self.__centerFrame.pack()
        self.initalizeLeftFrame()
        self.initalizeRightFrame()
        self.initalizeBottomFrame()

    def initalizeTopFrame(self,username):
        """Initializes top frame

        Args:
            username (string): stores username
        """
        self.__topFrame = Frame(self, bg=self.BACKGROUND_COLOR, width=1280, height=50)

        self.__usernameLabel = Label(self.__topFrame,text="User: "+username,bg=self.BACKGROUND_COLOR)
        self.__usernameLabel.grid(row=0,column=0,padx=110)

        #self.__comMode = OptionMenu(self.__topFrame, self.__currentPort, *self.SERIALCOMMODE)
        self.__comMode = ttk.Combobox(self.__topFrame, values= self.SERIALCOMMODE,state = "readonly")
        self.__comMode.grid(row=0,column=1,padx=5)
        self.__comButton = Button(self.__topFrame, text="Connect",bg="red", command=self.checkPort, relief="flat", padx=20)
        self.__comButton.grid(row=0,column=2,padx=5)
        self.__logoutButton = Button(self.__topFrame, text="Logout", command=self.logout, relief="flat", padx=20)
        self.__logoutButton.grid(row=0, column=3,padx=230)
        self.__topFrame.pack()
    def initalizeLeftFrame(self):
        self.__leftFrame = Frame(self.__centerFrame, bg=self.BACKGROUND_COLOR, width=640, height=550)
        self.__leftFrame.grid(row=0,column=0)
        self.__graphWindow = GraphWindow(self.__leftFrame)
        self.__graphWindow.pack()
    def initalizeRightFrame(self):
        self.__rightFrame = Frame(self.__centerFrame, bg=self.BACKGROUND_COLOR, width=640, height=550)
        self.__rightFrame.grid(row=0,column=1)
        topRight = Frame(self.__rightFrame, bg=self.BACKGROUND_COLOR, width=640, height=275)
        bottomRight = Frame(self.__rightFrame, bg=self.BACKGROUND_COLOR, width=640, height=275)
        topRight.pack()
        bottomRight.pack()
        self.__saveButton = Button(topRight, text="Select Mode", command=self.modeSelect, relief="flat", padx=20)
        self.__saveButton.grid(row=0, column=1, padx=20, pady=20)
        #self.__modeList = OptionMenu(topRight, self.__currentMode, *self.MODELABELS)
        self.__modeList = ttk.Combobox(topRight,values = self.MODELABELS,state="readonly")
        self.__modeList.grid(row=0, column=0, padx=20, pady=20)
        self.initalizeParameterList(bottomRight)
    def initalizeBottomFrame(self):
        self.__bottomFrame = Frame(self, bg=self.BACKGROUND_COLOR, width=1280, height=10)
        self.__bottomFrame.pack()
        self.__consoleLog = Button(self.__bottomFrame,text="Send",command="",relief="flat", padx=100)
        self.__consoleLog.grid(row=0, column=1, padx=20, pady=20)
        #self.__consoleLog = Text(self.__bottomFrame,width=100,height=5,state="disabled")
        #self.__consoleLog.pack(pady=10)
    
    def modeSelect(self):
        if self.__modeList.get() == "AOO":
            self.hideParameter(["readonly","readonly","readonly","disabled","readonly","disabled","disabled","disabled"])
        elif self.__modeList.get() == "AAI":
            self.hideParameter(["readonly","readonly","readonly","disabled","readonly","disabled","readonly","disabled"])
        elif self.__modeList.get() == "VOO":
            self.hideParameter(["readonly","readonly","disabled","readonly","disabled","readonly","disabled","disabled"])
        elif self.__modeList.get() == "VVI":
            self.hideParameter(["readonly","readonly","disabled","readonly","disabled","readonly","disabled","readonly"])

    def hideParameter(self,showState):
        for i in range(len(showState)):
            self.__entryArr[i].config(state = showState[i])

    def resetMode(self):
        self.__modeList.set("VOO")
        self.hideParameter(["readonly","readonly","disabled","readonly","disabled","disabled"])
        for item in self.__entryArr:
            item.set("")


    def checkPort(self):
        if self.__comMode.get() == "COM8":
            print("COM8 Selected")
            """self.__consoleLog.config(state="normal")
            self.__consoleLog.insert(tk.END,"COM8 Connected\n")
            self.__consoleLog.config(state="disabled")"""
        elif self.__comMode.get() == "COM9":
            print("COM9 Selected")
            """self.__consoleLog.config(state="normal")
            self.__consoleLog.insert(tk.END,"COM9 Connected\n")
            self.__consoleLog.config(state="disabled")"""

    def logout(self):
        self.__mainWindow.logout()
    def setUsername(self,username):
        self.__usernameLabel.config(text="User: " +username)
    
    def initalizeParameterList(self,higherFrame):
        #Initialzing all the parameter boxes
        for i in range(0,8,2):
            for j in range(2):
                label=Label(higherFrame,text=self.PARAMLABELS[i+j],bg=self.BACKGROUND_COLOR)
                entry = ttk.Combobox(higherFrame,values=self.PROGRAMABLEPARAMETERS[i+j],state="disabled")
                self.__labelArr.append(label)
                label.grid(row=i,column=j,padx=20,pady=10)
                self.__entryArr.append(entry)
                entry.grid(row=i+1,column=j,padx=20,pady=10)




"""
The ContentWindow stores all the visual components of the DCM
Extends tk.Frame
"""


class ContentWindow(tk.Frame):
    # Variables
    loginWindow = None
    parent = None
    DCM = None
    username = ""
    """
         Object Constructor
         @param self
    """

    def __init__(self,parent):
        tk.Frame.__init__(self,parent)
        self.parent=parent
        parent.title("DCM")
        parent.geometry("1000x600")
        parent.resizable(False,False)
        parent.config(bg='#FAF9F6')
        self.loginWindow = LoginWindow(self)
        self.DCM = DCMWindow(self,self.username)
        self.loginWindow.pack()

    def login(self):
        self.loginWindow.pack_forget()
        self.username = self.loginWindow.getUsername()
        self.DCM.setUsername(self.username)
        self.DCM.resetMode()
        self.DCM.pack()
    def logout(self):
        self.DCM.pack_forget()
        self.loginWindow.clearVal()
        self.loginWindow.setPaddingVisible()
        self.loginWindow.pack()

# Main script
if __name__ == "__main__":
    run = Run()

