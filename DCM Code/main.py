import tkinter
import tkinter as tk
from tkinter import *

"""
    The Run class is used to start the program
    @param none
"""


class Run:
    """
        Object Constructor
        @param self
    """

    def __init__(self):
        # The login window object is created
        LoginWindow()


"""
    The LoginWindow class is the the inital interface in viewing the program
    @param tk.Frame  
"""


class LoginWindow(tk.Tk):
    # Variable Declaration
    # Constants
    WIDTH = 30
    HEIGHT = 1
    FONT = ("Arial", 12)
    DEFAULT_USERNAME_TEXT = "Username"
    DEFAULT_PASSWORD_TEXT = "Password"
    DEFAULT_BUTTON_TEXT = "Submit"
    PADDING = 10
    # Private Variables
    __root = Tk()
    __usernameField = None
    __passwordField = None
    __submitButton = None
    __password = "Password"
    __username = "Username"
    __contentPane = None
    # Public Variables

    """
        Object Constructor
        @param self
    """

    def __init__(self):
        # Initialize components of frame
        self.__initializeEntryFields()
        self.__initializeButtons()

        self.__contentPane = PanedWindow(self.__root)
        self.__contentPane.pack(anchor=tkinter.CENTER)
        self.__contentPane.config(bg="red")
        # Initialize frame properties
        print()
        self.__root.title("DCM")
        self.__root.geometry("500x450")
        self.__root.config(bg='#0059b3')
        self.__root.mainloop()

    def __initializeEntryFields(self):
        self.__usernameField = Entry(self.__contentPane, width=self.WIDTH, font=self.FONT)
        self.__usernameField.insert(tk.END, self.DEFAULT_USERNAME_TEXT)
        self.__usernameField.pack(pady=self.PADDING)

        self.__passwordField = Entry(self.__contentPane, width=self.WIDTH, font=self.FONT, show="*")
        self.__passwordField.insert(tk.END, self.DEFAULT_PASSWORD_TEXT)
        self.__passwordField.pack(pady=self.PADDING)

    def __initializeButtons(self):
        self.__submitButton = Button(self.__contentPane, text=self.DEFAULT_BUTTON_TEXT, command=self.getText,
                                     relief="flat")
        self.__submitButton.pack()

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
            self.__contentPane.pack_forget()
            self.__submitButton.pack_forget()
            self.__passwordField.pack_forget()
            self.__usernameField.pack_forget()
            
        """


if __name__ == "__main__":
    run = Run()
