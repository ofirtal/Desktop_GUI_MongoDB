from db_gui.desktop_gui import Interface
from tkinter import *


"""  Not final. for now the main class only creates a gui object that interacts with MongoAtlasDB."""


class Main:
    def __init__(self):
        pass

    @staticmethod
    def create_gui():
        master = Tk()
        desktop_gui = Interface(master)
        mainloop()


if __name__ == '__main__':
    Main.create_gui()

