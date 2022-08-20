from ctypes.wintypes import HACCEL
from tkinter import *
from turtle import bgcolor, color
from PIL import ImageTk
from numpy import tensordot 
from tkinter import ttk

class add_std:
    def __init__(self , root):
        self.root = root 
        self.root.title("Exam Hall Allocations")
        self.root.geometry("1366x768+0+0")       
        self.root.config(background = "grey")
        self.root.state("zoomed")
        self.root.focus_force()



        self.searchicon = ImageTk.PhotoImage(file="icons/search.png" )
        self.headicon = ImageTk.PhotoImage(file="icons/dstd.png" )
        self.bg = ImageTk.PhotoImage(file="icons/bg3.jpg" )  
        self.add = ImageTk.PhotoImage(file="icons/add.png" )  
        self.upd = ImageTk.PhotoImage(file="icons/update.png" )  
        self.rem = ImageTk.PhotoImage(file="icons/delete.png" )  
         

    #=======================heading=====================

        self.heading = Label(self.root , image= self.headicon,  padx=10,compound= LEFT,text="Manage Students Details",font=('goudy old style',20,"bold"),bg="#341b64",fg="white")
        self.heading.place(x=0 , y=0 , width=1370   , height=50)

        self.bglbl = Label(self.root , image=self.bg).place(x=0 , y=50)

        self.namelbl = Label(self.root , text="Name" , font=("times new roman",15,"bold"),fg="white",bg="#c6033d").place(x=100,y=150)
        self.namelbl = Label(self.root , text="Roll No\n (Unique)" , font=("times new roman",15,"bold"),fg="white",bg="#ad0050").place(x=100,y=250)
        self.namelbl = Label(self.root , text="Department" , font=("times new roman",15,"bold"),fg="white",bg="#ad0050").place(x=100,y=350)
        self.namelbl = Label(self.root , text="LEVEL\n(I or II or III year)" , font=("times new roman",15,"bold"),fg="white",bg="#ad0050").place(x=50,y=450)

        self.nameentry = Entry(self.root , width=20 , fg="white" , bd=5 , bg="#61009f" , font=("goudy new style",19,"bold")).place(x=300 , y=150)
        self.nameentry = Entry(self.root , width=20 , fg="white" , bd=5 , bg="#61009f" , font=("goudy new style",19,"bold")).place(x=300 , y=250)
        self.nameentry = Entry(self.root , width=20 , fg="white" , bd=5 , bg="#61009f" , font=("goudy new style",19,"bold")).place(x=300 , y=350)
        self.nameentry = Entry(self.root , width=20 , fg="white" , bd=5 , bg="#61009f" , font=("goudy new style",19,"bold")).place(x=300 , y=450)

        #=================CURD btns===================

        self.addbtn = Button(self.root , text="ADD"   , image=self.add , compound=LEFT ,cursor="hand2", padx=5,activebackground="blue", font=("times",15,"bold"),width=100, fg="white" , bg="blue" ).place(x="100",y=550)
        self.updatebtn = Button(self.root , text="UPDATE" , font=("times",15,"bold") , cursor="hand2" ,  activebackground="green" ,width=100,image=self.upd , compound=LEFT , padx=5, fg="white" , bg="green" ).place(x="300",y=550)
        self.deletebtn = Button(self.root , text="DELETE" , font=("times",15,"bold"), cursor="hand2",activebackground='red',width=100,image=self.rem , compound=LEFT , padx=5, fg="white" , bg="red" ).place(x="100",y=650)
        self.clearbtn = Button(self.root , text="-    CLEAR" , font=("times",15,"bold"),width=10 , cursor="hand2", activebackground="grey", fg="white" , bg="grey" ).place(x="300",y=650)
        


        #-------------------------add std frames for data base-------------------
         
        #----------------serach panel---------

        self.srchlbl = Label(self.root  , text="ROLL NO" , font=("",19,"bold") , fg='black', bg="grey").place(x=700 , y=60)
        self.srchemt = Entry(self.root , width=15 , font=("sans-serif",15 ,"bold"),bg="grey" , fg="white" , bd=2 ).place(x=850 , y=60) 
        self.srchimg = Button(self.root , image=self.searchicon , bg="blue").place(x=1000 , y=60)


    #----------------------frame for database-----------

        self.Studentsframe = Frame(self.root, bd=2 , bg="black")
        self.Studentsframe.place(x= 660 , y=100  , width=700  , height=640)

        scrollx = Scrollbar(self.Studentsframe ,   orient=HORIZONTAL)
        scrolly = Scrollbar(self.Studentsframe , orient=VERTICAL)
       
        self.style = ttk.Style()
        self.style.configure("mystyle.Treeview" , rowhight=50 , font=("sans-serif",15) , bg="white" , fg="black")
        self.style.configure("mystyle.Treeview.Heading" , font=("sans-serif",15,"bold"),fg="black" , bg="white")
        self.StudentsTabel = ttk.Treeview(self.Studentsframe ,xscrollcommand=scrollx.set , yscrollcommand= scrolly.set , columns=('sid',"name","rollno" , "department" , "level") , style="mystyle.Treeview")
        
        self.StudentsTabel.heading("sid",text="S.ID")
        self.StudentsTabel.heading("name",text="NAME")
        self.StudentsTabel.heading("rollno",text="Roll No")
        self.StudentsTabel.heading("department",text="DEPARTMENTS")
        self.StudentsTabel.heading("level",text="LEVEL")
        self.StudentsTabel["show"] = 'headings'
        self.StudentsTabel.column("sid",width=100)
        self.StudentsTabel.column("rollno",width=200)
        self.StudentsTabel.column("department",width=200)
        self.StudentsTabel.column("level",width=100)
        scrollx.config(command= self.StudentsTabel.xview)
        scrolly.config(command=self.StudentsTabel.yview)
        scrollx.pack(side=BOTTOM , fill=X)
        scrolly.pack(side=RIGHT , fill=Y)
        self.StudentsTabel.pack(fill=BOTH , expand=1)
if __name__=="__main__":
    root = Tk()
    obj = add_std(root)    
    root.mainloop()