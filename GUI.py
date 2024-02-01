import tkinter as tk
import customtkinter as ctk

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title('Git')
        self.geometry('600x400')


        self.mainloop()


App()