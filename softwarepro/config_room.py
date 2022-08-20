from cProfile import label
import configparser
from tkinter import *
from PIL import ImageTk 
from add_department import add_departments
from add_room import rooms
from database_connection import add_rooms

class config_rooms:
    def __init__(self , root ):
        self.root = root
        self.root.state("zoomed")
        self.root.resizable(False , False)
        self.root.focus()      

        #========animartions===============
              
        def hover(e):
           self.adddepbtn["background"] = "blue"


        def leave(e):
            self.adddepbtn["background"] = "red"

        def hover1(e):
           self.addroomsbtn["background"] = "blue"


        def leave1(e):
            self.addroomsbtn["background"] = "red"

        def hover2(e):
           self.allocatehall["background"] = "blue"


        def leave2(e):
            self.allocatehall["background"] = "red"
                          

        #-------------------icons----------------------
        self.headicon = ImageTk.PhotoImage(file="icons/rooms.png" )
        self.mainbg = ImageTk.PhotoImage(file = "icons/configrooms_bg.jpeg")
        self.adddepicon = ImageTk.PhotoImage(file="icons/department2.png")
        self.addroomicon = ImageTk.PhotoImage(file="icons/rooms2.png" )
        self.allocateicon = ImageTk.PhotoImage(file="icons/stddetalis.png")
       #-------------headiung-----------------
        self.heading = Label(self.root , image= self.headicon,  padx=10,compound= LEFT,text="Configure Rooms",font=('goudy old style',20,"bold"),bg="grey",fg="white")
        self.heading.pack(fill=X)

      #-------------------labels---------------------------------
        self.bgimage = Label(self.root , image=self.mainbg)
        self.bgimage.place(x = 0 , y = 50)
  
        
      #--------------framews------------------------
        self.mainframe = Frame(self.root , background="black")
        self.mainframe.place(width = 600 , height=400 , x = 400 , y =200)

     #-----------------buttons--------------------
        self.adddepbtn = Button(self.mainframe  , cursor= "hand2", command=self.add_dep , image=self.adddepicon , compound=LEFT  , padx=10, fg="white", bg="red" ,text="Add Departments" , font=("sans-serif",15,"bold") , activebackground="#5f5aff" )
        self.adddepbtn.bind("<Enter>", hover)
        self.adddepbtn.bind("<Leave>", leave)
        self.adddepbtn.place(x=180 , y=70 , width=250 , height=50)


        self.addroomsbtn = Button(self.mainframe  ,cursor="hand2" ,command=self.add_rm , image=self.addroomicon,compound=LEFT , padx=10,  fg="white", bg="red" ,text="Add Rooms" , font=("sans-serif",15,"bold") , activebackground="#5f5aff" )
        self.addroomsbtn.bind("<Enter>", hover1)
        self.addroomsbtn.bind("<Leave>", leave1)
        self.addroomsbtn.place(x=180 , y=170 , width=250 , height=50)

        self.allocatehall = Button(self.mainframe , cursor="hand2" , image= self.allocateicon  , compound=LEFT , padx=10, fg="white", bg="red" ,text="Allocate Rooms" , font=("sans-serif",15,"bold") , activebackground="#5f5aff" )
        self.allocatehall.bind("<Enter>", hover2)
        self.allocatehall.bind("<Leave>", leave2)
        self.allocatehall.place(x=180 , y=270 , width=250 , height=50)

    def add_dep(self):
        self.new_win = Toplevel(self.root)
        self.add_dep = add_departments(self.new_win)
    
    def add_rm(self):
        self.new_win1 = Toplevel(self.root)
        self.add_roomde = rooms(self.new_win1)


if __name__=="__main__":
    root = Tk()
    obj = config_rooms(root)    
    root.mainloop()
     