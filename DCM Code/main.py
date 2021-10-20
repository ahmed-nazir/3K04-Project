import tkinter
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
    DEFAULT_SUBMIT_BUTTON_TEXT = "Submit"
    DEFAULT_REGISTER_BUTTON_TEXT = "Register"
    PADDING = 10
    BACKGROUND_COLOR = "#0059b3"
    PASSWORDFILE = "DCM Code\password.json"

    # Private Variables
    __root = None
    __mainWindow = None
    __usernameField = None
    __passwordField = None
    __submitButton = None
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
        self.__submitButton = Button(self.__buttonFrame, text=self.DEFAULT_SUBMIT_BUTTON_TEXT, command=self.getText,
                                   relief="flat")
                                   
        self.__submitButton.grid(row=0, column=0, padx=5, pady=10)

        self.__registerButton = Button(self.__buttonFrame, text=self.DEFAULT_REGISTER_BUTTON_TEXT,
                                       command=self.registerUser,
                                       relief="flat")
        self.__registerButton.grid(row=0, column=1, padx=5, pady=10)

        self.__buttonFrame.pack()

    """
        Function is called when the submit button is pressed, validates the password to the stored file and 
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
        self.CheckPass()
        #if(1):
         #   self.__mainWindow.login()

    def CheckPass(self):
        alt=FileIO(self.PASSWORDFILE)
        f=alt.readText()
        print(f)
        if self.__username in f:
            print("Works")
            if self.__password==f[self.__username]:
                self.__mainWindow.login()
            else:
                messagebox.askretrycancel("User Validation","Wrong password,try again?")
        else:
            messagebox.askyesno("User Validation","User not registered, do you want to register")
            self.registerUser()

            
        

    """
        Function opens a frame to add new credentials if applicable
        @param self
    """

    def registerUser(self):
        alt=FileIO(self.PASSWORDFILE)
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
    __buttonArr=[]
    __entryArr=[]
    def __init__(self, mainWindow):
        tk.Frame.__init__(self,mainWindow,bg="blue",width="1280",height="600")
        self.__topFrame= Frame(self,bg='blue',width=1280,height=50)
        self.__centerFrame = Frame(self,bg='blue',width=1280,height=550)
        self.__leftFrame = Frame(self.__centerFrame,bg='blue',width=640,height=550)
        self.__rightFrame = Frame(self.__centerFrame,bg='blue',width=640,height=550)
        self.__topFrame.pack()
        self.__centerFrame.pack()
        self.__leftFrame.grid(row=0,column=0)
        self.__rightFrame.grid(row=0,column=1)
        self.__graphWindow = GraphWindow(self.__leftFrame)
        self.__graphWindow.pack()
        self.initalizeButtonList()
    def initalizeButtonList(self):
        for i in range(0,8,2):
            for j in range(2):
                label=Label(self.__rightFrame,text=i+j)
                entry = Entry(self.__rightFrame)
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
        parent.geometry("1200x600")
        parent.config(bg='#0059b3')
        self.loginWindow = LoginWindow(self)
        #self.frame=Frame(self,bg="red",width=112,height=112)
        #self.frame.pack(anchor='center')
        self.loginWindow.pack(anchor="s")

    def login(self):
        self.loginWindow.pack_forget()
        self.loginWindow.destroy()
        self.DCM =DCMWindow(self)
        self.DCM.pack()

# Main script
if __name__ == "__main__":
    run = Run()
