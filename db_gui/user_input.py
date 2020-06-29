from tkinter import *


class UserInput:
    """ gui user input fields """
    def __init__(self, root, f_row, f_column, data):
        self.root = root
        self.frame = Frame(root)
        self.frame.grid(row=f_row, column=f_column)

        self.data_lbl = Label(self.frame, text=str(data), width=20)
        self.user_data = Entry(self.frame, width=20)

        self.data_lbl.grid(row=0, column=0)
        self.user_data.grid(row=0, column=1)

    def clear(self):
        self.user_data.delete(0, END)

    def get_user_data(self):
        return self.user_data.get()
