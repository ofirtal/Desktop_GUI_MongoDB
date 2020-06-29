from tkinter import *


class ControlPanel:
    """ gui control panel buttons - clear, submit and delete"""

    def __init__(self, root, f_row, f_column, button_command_clear, button_command_submit, delete_from_db):
        self.root = root
        self.frame = Frame(root)
        self.frame.grid(row=f_row, column=f_column)

        self.clear = Button(self.frame, text='Clear', width=10, command=button_command_clear)
        self.submit = Button(self.frame, text='Submit', width=10, command=button_command_submit)
        self.delete_user = Button(self.frame, text='Delete User from DB', width=16,  command=delete_from_db)

        self.submit.grid(row=0, column=0)
        self.clear.grid(row=0, column=1)
        self.delete_user.grid(row=0, column=2)

