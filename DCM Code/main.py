import tkinter
import tkinter as tk
from tkinter import *
from tkinter import messagebox

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
        tk.Frame.__init__(self,mainWindow)
        self.__mainWindow = mainWindow
        self.__root = mainWindow
        # Initialize components of frame
        self.__initializeEntryFields()
        self.__initializeButtons()

        self.__contentPane = Frame(self.__root, bg="red")
        self.__contentPane.pack(anchor=tkinter.CENTER)
        # Initialize frame properties
        self.__root.config(bg=self.BACKGROUND_COLOR)

    """
        Initializes the text fields and adds formatting to them
        @param self
    """

    def __initializeEntryFields(self):
        self.__usernameField = Entry(self.__contentPane, width=self.WIDTH, font=self.FONT)
        self.__usernameField.insert(tk.END, self.DEFAULT_USERNAME_TEXT)
        self.__usernameField.pack(pady=self.PADDING)

        self.__passwordField = Entry(self.__contentPane, width=self.WIDTH, font=self.FONT, show="*")
        self.__passwordField.insert(tk.END, self.DEFAULT_PASSWORD_TEXT)
        self.__passwordField.pack(pady=self.PADDING)

    """
       Initializes the buttons and adds formatting to them
       @param self
    """

    def __initializeButtons(self):
        self.__buttonFrame = Frame(self.__contentPane, bg=self.BACKGROUND_COLOR)
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
        """
        if(1):
            
        """

    """
        Function opens a frame to add new credentials if applicable
        @param self
    """

    def registerUser(self):
        pass

    """
    Getter functions
    """

    def getRoot(self):
        return self.__root


"""
    Frame to enter a new password and username to the storage file
"""


class RegisterWindow(tk.Frame):
    pass


"""
The ContentWindow stores all the visual components of the DCM
Extends tk.Tk
"""


class ContentWindow(tk.Frame):
    # Variables
    loginWindow = None
    """
         Object Constructor
         @param self
    """

    def __init__(self,parent):
        tk.Frame.__init__(self,parent)
        parent.title("DCM")
        parent.geometry("500x450")
        parent.config(bg='#0059b3')

        loginWindow = LoginWindow(self)

    def login(self):
        pass

# Main script
if __name__ == "__main__":
    #run = Run()
    io = FileIO("password.txt",'w')
    Dict = {"Hello":"World"}
    print(type(Dict))
    io.writeText(Dict)
    print(type(io.readText()))
