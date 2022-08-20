from msilib.schema import File
from textwrap import fill 
#from turtle import widthrprr
from PIL import Image, ImageTk
from cProfile import label
from tkinter import *
from tkinter import  ttk
from add_stds import add_stds
from add_staff import add_staff
from config_room import config_rooms
from database_connection import std_database , staff_database , add_dep , add_rooms

std_db = std_database("databases//students_data.db")
staff_db = staff_database("databases//staff_data.db")
dep_db = add_dep("databases//departments_data.db")
rooms_db = add_rooms("databases//rooms_details.db")


class app:
    def __init__(self , root):
        self.root = root 
        self.root.title("Exam Hall Allocations")
        self.root.geometry("1090x600+100+50")       
        self.root.config(background = "white")
        self.root.resizable(False , False)
        
   
        def hover(e):
           self.staffbtn["background"] = "blue"


        def leave(e):
            self.staffbtn["background"] = "black"
                

        def hover1(e):
               self.stdbtn["background"] = "blue"


        def leave1(e):
            self.stdbtn["background"] = "black"
                
        def hover2(e):
            self.configroomsbtn["background"] = "blue"


        def leave2(e):
            self.configroomsbtn["background"] = "black"
                
    
        def hover3(e):
            self.reportbtn["background"] = "blue"


        def leave3(e):
            self.reportbtn["background"] = "black"  
    
        def hover4(e):
            self.logoutbtn["background"] = "#ff0004"


        def leave4(e):
            self.logoutbtn["background"] = "black"  
    
        
        #=========================icons============================
        self.headicon = ImageTk.PhotoImage(file="icons/headicon.jpg" )
        self.dashicon = ImageTk.PhotoImage(file="icons/dash.png" )
        self.stdicon = ImageTk.PhotoImage(file="icons/students.png" )
        self.roomsicon = ImageTk.PhotoImage(file="icons/exsam.png" )
        self.settingsicon = ImageTk.PhotoImage(file="icons/setings.png" )
        self.logouticon = ImageTk.PhotoImage(file="icons/logout.png" )
        self.dashbg =  ImageTk.PhotoImage(file="icons/dashbg.jpg" )
        self.stdfrmbg = ImageTk.PhotoImage(file="icons/bg.jpg" )
        self.report = ImageTk.PhotoImage(file="icons/report.png" ) 
        self.dashstdicon = ImageTk.PhotoImage(file="icons/dstd.png" ) 
        self.dashstafficon = ImageTk.PhotoImage(file="icons/dstaff.png" ) 
        self.departmentsicon = ImageTk.PhotoImage(file="icons/department.png" ) 
        self.droomsicon = ImageTk.PhotoImage(file="icons/rooms.png" ) 
        #-------------------heading------------------------

        self.heading = Label(self.root , image= self.headicon,  padx=10,compound= LEFT,text="Exam Hall Alertment",font=('goudy old style',20,"bold"),bg="#341b64",fg="white")
        self.heading.place(x=0 , y=0 , width=1100   , height=50)

        self.nav_bar = Frame(self.root  , width= 1100 , height=50 , background = "black")               
        self.nav_bar.place(x=0  , y=50 )
        
        self.nav_frame = Frame(self.root ,bg="black", width = 300 , height=500)
        self.nav_frame.place(x=0 , y = 100 )

        self.dashlbl = Label(self.nav_bar ,  text="Dashboard" , compound= LEFT , padx=10,image=self.dashicon, font=("sans-serif",15,"bold") , bg="black" , fg="white")
        self.dashlbl.place(x = 10 , y=10)

        self.stdbtn = Button(self.nav_frame , image=self.stdicon  , command=self.add_students, compound=LEFT,padx=10 ,  fg="white", bg="black" ,text="Add Students" , font=("sans-serif",10,"bold") , activebackground="#5f5aff" , width = 300 , height=50, bd=0)
        self.stdbtn.bind("<Enter>", hover1)
        self.stdbtn.bind("<Leave>", leave1)
        self.stdbtn.place(x=0 , y=50 )


        self.staffbtn = Button(self.nav_frame , command= self.add_staff, padx=10, image=self.roomsicon , compound=LEFT  , fg="white", bg="black" ,text="Add Staff" , font=("sans-serif",10,"bold") , width = 300 ,height=50 , bd=0 , activebackground="#5f5aff" )
        self.staffbtn.bind("<Enter>", hover)
        self.staffbtn.bind("<Leave>", leave)
        self.staffbtn.place(x=0 , y=150)


        self.configroomsbtn = Button(self.nav_frame ,padx=10, command= self.configroom, image=self.settingsicon, compound=LEFT,fg="white", bg="black" ,text="Config Rooms" , font=("sans-serif",10,"bold") , width = 300 , height=50 ,  bd=0 , activebackground="#5f5aff")
        self.configroomsbtn.bind("<Enter>", hover2)
        self.configroomsbtn.bind("<Leave>", leave2)
        self.configroomsbtn.place(x=0 , y=240 )

        self.reportbtn = Button(self.nav_frame , padx=10 , image=self.report, compound=LEFT,fg="white", bg="black" ,text="Reports" , font=("sans-serif",10,"bold") , width = 300 , height=50 ,  bd=0 , activebackground="#5f5aff")
        self.reportbtn.bind("<Enter>", hover3)
        self.reportbtn.bind("<Leave>", leave3)
        self.reportbtn.place(x=0 , y=340 )

        self.logoutbtn = Button(self.nav_bar  , image=self.logouticon, command=root.quit ,padx=10 ,  compound=LEFT,fg="white", bg="black" ,text="Logout" , font=("sans-serif",10,"bold") , width = 120 , bd=0 , activebackground="#5f5aff")
        self.logoutbtn.bind("<Enter>", hover4)
        self.logoutbtn.bind("<Leave>", leave4)
        self.logoutbtn.place(x=916 , y=15 )


        
        
        self.dashbgimg = Label(image=self.dashbg)
        self.dashbgimg.place(x=301 , y=100)

        #=============dashboard frames============
        
        val = std_db.counting()[0]

        

        self.stdcountlbl=Label(self.root , image=self.stdfrmbg , bd=0)
        self.stdcountlbl.place(x=400 , y = 120)
        self.stdcunticon = Label(root , image=self.dashstdicon , bg="red" )
        self.stdcunticon.place(x=520 , y = 140 )
        self.stdcuntlbl = Label(root, text=f"TOATAL STUDENTS \n {val}" , font=("",19,"bold") , bg="red" , fg="white")
        self.stdcuntlbl.place(x=420 , y=200)

        val1 = staff_db.counting()[0]


        self.staffcountlbl=Label(self.root , image=self.stdfrmbg , bd=0)
        self.staffcountlbl.place(x=750 , y = 120)
        self.staffcunticon = Label(root , image=self.dashstafficon , bg="red" )
        self.staffcunticon.place(x=880 , y = 140 )
        self.staffcuntlbl = Label(root, text=f"TOATAL STAFFS \n {val1}" , font=("",19,"bold") , bg="red" , fg="white")
        self.staffcuntlbl.place(x=800 , y=200)

        val2 = rooms_db.counting()[0]

        self.stdcountlbl=Label(self.root , image=self.stdfrmbg , bd=0)
        self.stdcountlbl.place(x=400 , y = 350)
        self.stdcunticon = Label(root , image=self.droomsicon , bg="red" )
        self.stdcunticon.place(x=520 , y = 380 )
        self.stdcuntlbl = Label(root, text=f"TOATAL ROOMS \n {val2}" , font=("",19,"bold") , bg="red" , fg="white")
        self.stdcuntlbl.place(x=440 , y=450)

        val3 = dep_db.counting()[0]

        self.stdcountlbl=Label(self.root , image=self.stdfrmbg , bd=0)
        self.stdcountlbl.place(x=750 , y = 350)
        self.stdcunticon = Label(root , image=self.departmentsicon , bg="red" )
        self.stdcunticon.place(x=870 , y = 380 )
        self.stdcuntlbl = Label(root, text=f"TOATAL DEPARTMENT \n {val3}" , font=("",19,"bold") , bg="red" , fg="white")
        self.stdcuntlbl.place(x=750 , y=450)

    def add_students(self):
        self.new_win1 = Toplevel(root)
        self.add_student = add_stds(self.new_win1)

    def add_staff(self):
        self.new_win2 = Toplevel(root)
        self.add_student = add_staff(self.new_win2)    
        
    def configroom(self):
        self.new_win3 = Toplevel(self.root)
        self.congfigroom = config_rooms(self.new_win3)           





if __name__=="__main__":
    root = Tk()
    obj = app(root)    
    root.mainloop()


















































































        