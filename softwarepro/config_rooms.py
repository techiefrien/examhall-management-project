from tkinter import *

class config_room:
    def __init__(self , root):
        self.root = root
        self.root.state("zoomed")
        self.root.resizable(False , False)


          




if __name__ == "__main__":
    root = Tk()
    obj = config_room(root)
    root.mainloop()
