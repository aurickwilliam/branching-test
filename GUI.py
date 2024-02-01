import tkinter as tk
import customtkinter as ctk

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title('Git')
        self.geometry('600x400')
        self.minsize(600, 400)
        ctk.set_appearance_mode('Dark')
        ctk.set_default_color_theme('green')

        self.button = ctk.CTkButton(self, text= 'Button')
        self.button.pack(expand= True)

        self.mainloop()


App()