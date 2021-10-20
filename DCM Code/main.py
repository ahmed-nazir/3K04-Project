import tkinter as tk
from tkinter import *
from tkinter import messagebox
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
NavigationToolbar2Tk)
from IOStream import FileIO

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
    BACKGROUND_COLOR = "#0059b3"

    # Private Variables
    __root = None
    __mainWindow = None
    __usernameField = None
    __passwordField = None
    __loginButton = None
    __registerButton = None
    __password = "Password"
    __username = "Username"
    __contentPane = None
    __buttonFrame = None
    # Public Variables

    """
        Object Constructor
        @param self
    """

    def __init__(self, mainWindow):
        tk.Frame.__init__(self,mainWindow,bg="red",padx=50,pady=50)
        self.__mainWindow = mainWindow
        self.__root = mainWindow
        # Initialize components of frame
        self.__initializeEntryFields()
        self.__initializeButtons()
        # Initialize frame properties
        self.__root.config(bg=self.BACKGROUND_COLOR)

    """
        Initializes the text fields and adds formatting to them
        @param self
    """

    def __initializeEntryFields(self):
        self.__usernameField = Entry(self, width=self.WIDTH, font=self.FONT)
        self.__usernameField.insert(tk.END, self.DEFAULT_USERNAME_TEXT)
        self.__usernameField.pack(pady=self.PADDING)

        self.__passwordField = Entry(self, width=self.WIDTH, font=self.FONT, show="*")
        self.__passwordField.insert(tk.END, self.DEFAULT_PASSWORD_TEXT)
        self.__passwordField.pack(pady=self.PADDING)

    """
       Initializes the buttons and adds formatting to them
       @param self
    """

    def __initializeButtons(self):
        self.__buttonFrame = Frame(self, bg="red")
        self.__loginButton = Button(self.__buttonFrame, text=self.DEFAULT_login_BUTTON_TEXT, command=self.getText,
                                   relief="flat")
        self.__loginButton.grid(row=0, column=0, padx=5, pady=10)

        self.__registerButton = Button(self.__buttonFrame, text=self.DEFAULT_REGISTER_BUTTON_TEXT,
                                       command=self.registerUser,
                                       relief="flat")
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
        # DEBUGGING: Test output, remove when no longer needed
        print(self.__username, " Username")
        print(self.__password, " Password")

        # Code below is when there is a matching password and key, the program
        # will remove the password screen and add the main program
        # --Note: figure out a way to only remove content pane instead of removing all elements in content pane

        if(1):
            self.__mainWindow.login()

    def CheckPass(self):
        alt=FileIO(self.__filename,"r")
        f=alt.readText()
        if self.__username in f:
            if self.__password==f[self.__username]:
                self.__mainWindow.login()
            else:
                messagebox.askretrycancel("User Validation","Wrong password,try again?")
        else:
            messagebox.askyesno("User Validation","User not registered, do you want to register?")
            self.registerUser()

            
        

    """
        Function opens a frame to add new credentials if applicable
        @param self
    """

    def registerUser(self):
        alt=FileIO(__filename,"r")
        d=alt.getlength()
        text={self.__username:self.__password}
        if d==10:
            messagebox.showinfo("User Validation","Maximum number of users reached")
        else:
            alt.writeText(text)
                                

    """
    Getter functions
    """

    def getRoot(self):
        return self.__root


"""
    Frame to enter a new password and username to the storage file
"""


class RegisterWindow(tk.Frame):

    """
        Object Constructor
        @param self
    """

    def __init__(self, mainWindow):
        tk.Frame.__init__(self, mainWindow)

class GraphWindow(tk.Frame):
    __mainWindow=None
    def __init__(self, mainWindow):
        tk.Frame.__init__(self, mainWindow, bg="yellow", width="640", height="550")
        self.__mainWindow = mainWindow
        self.plot()
    def plot(self):
            # the figure that will contain the plot
            fig = Figure(figsize=(4, 4),
                         dpi=100)

            # list of squares
            y = [i ** 2 for i in range(101)]

            # adding the subplot
            plot1 = fig.add_subplot(111)

            # plotting the graph
            plot1.plot(y)

            # creating the Tkinter canvas
            # containing the Matplotlib figure
            canvas = FigureCanvasTkAgg(fig,
                                       master=self)
            canvas.draw()

            # placing the canvas on the Tkinter window
            canvas.get_tk_widget().pack()

            # creating the Matplotlib toolbar
            toolbar = NavigationToolbar2Tk(canvas,
                                           self)
            toolbar.update()

            # placing the toolbar on the Tkinter window
            canvas.get_tk_widget().pack()

class DCMWindow(tk.Frame):
    # Constants
    PARAMLABELS = ["Lower Rate Limit","Upper Rate Limit","Atrial Amplitude","Atrial Pulsewidth","Atrial Refractory Period","Ventricular Amplitude","Ventricular Pulsewidth","Ventricular Refractory Period"]
    MODELABELS = {"AOO", "VOO", "AAI", "VVI" }
    #The following variable is a placeholder before serial communication is implemented
    SERIALCOMMODE = {"COM8","COM9"}
    # Padding is in PX
    PADDING = 20
    # Private Variables
    __buttonArr=[]
    __entryArr=[]
    __modeList = None
    __currentMode = None
    __currentPort = None

    __saveButton = None
    __comMode = None

    """
        Constructor
        @param mainWindow
    """

    def __init__(self, mainWindow):
        tk.Frame.__init__(self,mainWindow,bg="blue",width=1280,height=600)
        self.__topFrame= Frame(self,bg='blue',width=1280,height=50)
        self.__centerFrame = Frame(self,bg='blue',width=1280,height=550)
        self.__leftFrame = Frame(self.__centerFrame,bg='blue',width=640,height=550)
        self.__rightFrame = Frame(self.__centerFrame,bg='blue',width=640,height=550)
        self.__topFrame.pack()
        self.__centerFrame.pack()
        self.__leftFrame.grid(row=0,column=0)
        self.__rightFrame.grid(row=0,column=1)


        topRight= Frame(self.__rightFrame,bg='blue',width=640,height=275)
        bottomRight = Frame(self.__rightFrame, bg='blue', width=640, height=275)
        topRight.pack()
        bottomRight.pack()
        self.__saveButton= Button(topRight,text="Save Mode",command="", relief="flat",padx=20)
        self.__saveButton.grid(row=0,column=1,padx=20,pady=20)
        self.__currentMode=StringVar(self)
        self.__currentPort = StringVar(self)

        self.__modeList = OptionMenu(topRight,self.__currentMode,* self.MODELABELS)
        self.__modeList.grid(row=0,column=0,padx=20,pady=20)
        self.__graphWindow = GraphWindow(self.__leftFrame)
        self.__graphWindow.pack()

        self.__comMode=OptionMenu(self.__topFrame,self.__currentPort,* self.SERIALCOMMODE)
        self.__comMode.pack(fill=Y)
        self.initalizeButtonList(bottomRight)

    def initalizeButtonList(self,higherFrame):
        for i in range(0,8,2):
            for j in range(2):
                label=Label(higherFrame,text=self.PARAMLABELS[i+j])
                entry = Entry(higherFrame)
                self.__buttonArr.append(label)
                label.grid(row=i,column=j,padx=20,pady=20)
                self.__entryArr.append(entry)
                entry.grid(row=i+1,column=j,padx=20,pady=20)



"""
The ContentWindow stores all the visual components of the DCM
Extends tk.Frame
"""


class ContentWindow(tk.Frame):
    # Variables
    loginWindow = None
    parent = None
    DCM = None
    """
         Object Constructor
         @param self
    """

    def __init__(self,parent):
        tk.Frame.__init__(self,parent)
        self.parent=parent
        parent.title("DCM")
        parent.geometry("1280x600")
        parent.config(bg='#0059b3')
        self.loginWindow = LoginWindow(self)
        self.loginWindow.pack(anchor="s")

    def login(self):
        self.loginWindow.pack_forget()
        self.loginWindow.destroy()
        self.DCM =DCMWindow(self)
        self.DCM.pack()

# Main script
if __name__ == "__main__":
    run = Run()
