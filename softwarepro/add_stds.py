from email.errors import MessageError
from logging import exception
from multiprocessing.sharedctypes import Value
from tkinter import *
from turtle import width
from PIL import ImageTk 
from tkinter import ttk , messagebox
import sqlite3
from numpy import add
from database_connection import std_database , add_dep
import sqlite3

global db , db1

db = std_database("databases//students_data.db")
db1 = add_dep("databases//departments_data.db")

class add_stds:
    def __init__(self , root ):
        self.root = root
        self.root.state("zoomed")
        self.root.resizable(False , False)
        self.root.focus()      

        #------------cions load----------
        self.headicon = ImageTk.PhotoImage(file="icons/dstd.png" )
        self.clearicon = ImageTk.PhotoImage(file="icons/clear.png")
        self.searchicon = ImageTk.PhotoImage(file="icons/search.png" )
        self.headicon = ImageTk.PhotoImage(file="icons/dstd.png" )
        self.bg = ImageTk.PhotoImage(file="icons/bg3.jpg" )  
        self.add = ImageTk.PhotoImage(file="icons/add.png" )  
        self.upd = ImageTk.PhotoImage(file="icons/update.png" )  
        self.rem = ImageTk.PhotoImage(file="icons/delete.png" )  
        self.xlsicon = ImageTk.PhotoImage(file="icons/xl.png")
         
       #------------------------heading------
        self.heading = Label(self.root , image= self.headicon,  padx=10,compound= LEFT,text="Manage Students Details",font=('goudy old style',20,"bold"),bg="#b246ff",fg="black")
        self.heading.pack(fill=X)

      #------------------------variable---------------
        self.std_name = StringVar()
        self.std_roll = StringVar()
        self.std_department = StringVar()
        self.std_level = StringVar()  
        self.search = StringVar()
  
       #---------------frames-------
        self.input_frame = Frame(self.root , background="black" , height=350 , width = 1366 )
        self.input_frame.place(x=0 , y=50 )
        #self.output_frame = Frame(background="white" , height=350 , width = 1366 )
        #self.output_frame.place(x=0 , y=400 )

      #==============labels and inputfld in input frams================
        self.namelbl = Label(self.root , text="Name" , font=("times new roman",15,"bold"),fg="white",bg="black").place(x=100,y=100)
        self.rollnumlbl = Label(self.root , text="Roll No\n (Unique)" , font=("times new roman",15,"bold"),fg="white",bg="black").place(x=700,y=100)
        self.departmentlbl = Label(self.root , text="Department" , font=("times new roman",15,"bold"),fg="white",bg="black").place(x=100,y=200)
        self.yearlbl = Label(self.root , text="LEVEL\n(I or II or III year)" , font=("times new roman",15,"bold"),fg="white",bg="black").place(x=660,y=200)
        
        val =  db1.list_items()
        val = tuple(val)
        
            
        



        self.nameentry = Entry(self.root , textvariable=self.std_name,  width=20 , fg="black" , bd=5 , bg="white" , font=("goudy new style",19,"bold")).place(x=250 , y=100)
        self.rollnumentry = Entry(self.root  , textvariable=self.std_roll, width=20 , fg="black" , bd=5 , bg="white" , font=("goudy new style",19,"bold")).place(x=900, y=100)
        self.department_list = ttk.Combobox(self.root ,state="Readonly", textvariable=self.std_department , values=val   , font=("goudy new style",20,"bold")).place(x=250, y=200 , width = 300 , height=40 )
        self.year_list = ttk.Combobox(self.root ,textvariable=self.std_level,  font=("goudy new style",20,"bold"), values= ("I Year" , "II Year" , "III Year") ).place(x=900 , y=200 , width=300)

       #=====================buttons slot====================
        self.addbtn = Button(self.root, state = "active",command=self.addrec , text="ADD Details"   , image=self.add , compound=LEFT ,cursor="hand2", padx=5,activebackground="blue", font=("times",15,"bold") ,width=200, fg="white" , bg="blue" ).place(x=10,y=340)
        self.updatebtn = Button(self.root ,command=self.updrec, state = "disabled", text="UPDATE Details" , font=("times",15,"bold") , cursor="hand2" ,  activebackground="green" ,width=200,image=self.upd , compound=LEFT , padx=5, fg="white" , bg="green" ).place(x=250,y=340)
        self.deletebtn = Button(self.root ,command=self.deleterec, state = "disabled", text="DELETE Details" , font=("times",15,"bold"), cursor="hand2",activebackground='red',width=200,image=self.rem , compound=LEFT , padx=5, fg="white" , bg="red" ).place(x=490,y=340)
        self.clearbtn = Button(self.root , command=self.clearall,text="CLEAR Details" , image=self.clearicon, compound=LEFT, font=("times",15,"bold"),width=200 , cursor="hand2", activebackground="orange", padx=5 ,fg="white" , bg="orange" ).place(x=730,y=340)
        self.savebtn = Button(self.root , command=self.save_xl,text="Save" , image=self.xlsicon, compound=LEFT, font=("times",15,"bold"),width=100 , cursor="hand2", activebackground="green", padx=10 ,fg="white" , bg="green" ).place(x=965,y=340)
        
        #self.srchlbl = Label(self.root  , text="ROLL NO" , font=("",19,"bold") , fg='black', bg="grey").place(x=800 , y=60)
        #self.srchemt = Entry(self.root , width=15 , font=("sans-serif",15 ,"bold"),bg="grey" , fg="white" , bd=2 ).place(x=1000 , y=340) 
        self.searchentry = Entry(self.root , textvariable=self.search , width=20 , fg="black" , bd=5 , bg="white" , font=("goudy new style",15,"bold")).place(x=1100,y=340)
        self.srchbtn = Button(self.root , image=self.searchicon , bg="blue" , command=self.searchfrmdb)
        self.srchbtn.place(x=1320 , y=340)

        
        #===================database info==========================
        
        self.Studentsframe = Frame(self.root , bd=2 , bg="black")
        self.Studentsframe.place(x= 0 , y=390  , width=1366  , height=350)

        scrollx = Scrollbar(self.Studentsframe ,   orient=HORIZONTAL)
        scrolly = Scrollbar(self.Studentsframe , orient=VERTICAL)
       
        self.style = ttk.Style()
        self.style.configure("mystyle.Treeview" , rowheight = 50 , font=("sans-serif",15) , bg="white" , fg="black")
        self.style.configure("mystyle.Treeview.Heading" , font=("sans-serif",15,"bold"),fg="black" , bg="white")
        self.StudentsTabel = ttk.Treeview(self.Studentsframe ,xscrollcommand=scrollx.set , yscrollcommand= scrolly.set , columns=('sid',"names","rollnumber" , "department" , "levels") , style="mystyle.Treeview")
        
        self.StudentsTabel.heading("sid",text="S.ID")
        self.StudentsTabel.heading("names",text="NAME")
        self.StudentsTabel.heading("rollnumber",text="Roll No")
        self.StudentsTabel.heading("department",text="DEPARTMENTS")
        self.StudentsTabel.heading("levels",text="LEVEL")
        self.StudentsTabel["show"] = 'headings'
        self.StudentsTabel.column("sid",width=10)
        self.StudentsTabel.column("names",width=280)
        self.StudentsTabel.column("rollnumber",width=200)
        self.StudentsTabel.column("department",width=200)
        self.StudentsTabel.column("levels",width=100)
        self.StudentsTabel.bind("<ButtonRelease-1>",self.getData)
        scrollx.config(command= self.StudentsTabel.xview)
        scrolly.config(command=self.StudentsTabel.yview)
        scrollx.pack(side=BOTTOM , fill=X)
        scrolly.pack(side=RIGHT , fill=Y)
        
        self.StudentsTabel.pack(fill=BOTH , expand=1)
        self.displayall()
        self.autosrch()
        
#================== sub functions ===========================
    

    def getData(self,event):
        currnet_row = self.StudentsTabel.focus()
        data =  self.StudentsTabel.item(currnet_row)     
        global rows 
        rows = data["values"]

        self.std_name.set(rows[1])
        self.std_roll.set(rows[2])
        self.std_department.set(rows[3])
        self.std_level.set(rows[4])
        self.addbtn = Button(self.root, state = "disabled",command=self.addrec , text="ADD Details"   , image=self.add , compound=LEFT ,cursor="hand2", padx=5,activebackground="blue", font=("times",15,"bold") ,width=200, fg="white" , bg="blue" ).place(x=10,y=340)
        self.updatebtn = Button(self.root ,command=self.updrec, state = "active", text="UPDATE Details" , font=("times",15,"bold") , cursor="hand2" ,  activebackground="green" ,width=200,image=self.upd , compound=LEFT , padx=5, fg="white" , bg="orange" ).place(x=250,y=340)
        self.deletebtn = Button(self.root ,command=self.deleterec, state = "active", text="DELETE Details" , font=("times",15,"bold"), cursor="hand2",activebackground='red',width=200,image=self.rem , compound=LEFT , padx=5, fg="white" , bg="red" ).place(x=490,y=340)
       
    
    def displayall(self):
        self.StudentsTabel.delete(*self.StudentsTabel.get_children())  
        for row in db.fetch():
            self.StudentsTabel.insert("", END , values=row)
        
  

    def clearall(self):
        
      self.std_name.set("")
      self.std_roll.set("")
      self.std_department.set("")
      self.std_level.set("")        

    def addrec(self):
        
      
        if self.std_name.get()=="" or self.std_roll.get()=="" or self.std_department.get()=="" or self.std_level.get()=="":
            messagebox.showerror('error',"please fill the all details" , parent = self.root)
            
        
        
        else:
            rollnum = self.std_roll.get().upper()
            department=self.std_department.get().replace("{","")
            department = self.std_department.get().replace("{ }","")
            db.insert(self.std_name.get(),rollnum,department,self.std_level.get()) 
            self.displayall()         
            self.clearall()
            messagebox.showinfo("Success","Record Added Successfuly" , parent = self.root)

    def deleterec(self):
        if self.std_name.get()=="" or self.std_roll.get()=="" or self.std_department.get()=="" or self.std_level.get()=="":
            messagebox.showerror('error',"please Select the data to delete" , parent= self.root)
            
        else:  
            std_database.remove(db,rows[0])
            self.displayall()         
            self.clearall()
            messagebox.showinfo("Success","Record deleted successfuly" , parent = self.root)
            self.addbtn = Button(self.root, state = "active",command=self.addrec , text="ADD Details"   , image=self.add , compound=LEFT ,cursor="hand2", padx=5,activebackground="blue", font=("times",15,"bold") ,width=200, fg="white" , bg="blue" ).place(x=10,y=340)
            self.updatebtn = Button(self.root ,command=self.updrec, state = "disabled", text="UPDATE Details" , font=("times",15,"bold") , cursor="hand2" ,  activebackground="green" ,width=200,image=self.upd , compound=LEFT , padx=5, fg="white" , bg="orange" ).place(x=250,y=340)
            self.deletebtn = Button(self.root ,command=self.deleterec, state = "disabled", text="DELETE Details" , font=("times",15,"bold"), cursor="hand2",activebackground='red',width=200,image=self.rem , compound=LEFT , padx=5, fg="white" , bg="red" ).place(x=490,y=340)
       

    def updrec(self):
        if self.std_name.get()=="" or self.std_roll.get()=="" or self.std_department.get()=="" or self.std_level.get()=="":
            messagebox.showerror('error',"please select the data the record to update" , parent = self.root)  
        
        
        else:
            rollnum = self.std_roll.get().upper()
            db.update(rows[0],self.std_name.get(),rollnum,self.std_department.get(),self.std_level.get()) 
            self.displayall()         
            self.clearall()
            messagebox.showinfo("Success","Record Updated Successfuly")
            self.addbtn = Button(self.root, state = "active",command=self.addrec , text="ADD Details"   , image=self.add , compound=LEFT ,cursor="hand2", padx=5,activebackground="blue", font=("times",15,"bold") ,width=200, fg="white" , bg="blue" ).place(x=10,y=340)
            self.updatebtn = Button(self.root ,command=self.updrec, state = "disabled", text="UPDATE Details" , font=("times",15,"bold") , cursor="hand2" ,  activebackground="green" ,width=200,image=self.upd , compound=LEFT , padx=5, fg="white" , bg="orange" ).place(x=250,y=340)
            self.deletebtn = Button(self.root ,command=self.deleterec, state = "disabled", text="DELETE Details" , font=("times",15,"bold"), cursor="hand2",activebackground='red',width=200,image=self.rem , compound=LEFT , padx=5, fg="white" , bg="red" ).place(x=490,y=340)
       

    def searchfrmdb(self):
        rollnumber = self.search.get()
        if self.search.get() =="" :
            messagebox.showerror("error","please enter the student roll number" , parent= self.root )
            self.displayall()
        elif db.validate(rollnumber)==[]:
            messagebox.showerror('error',"Reord not found",parent=self.root)
        else:
            self.autosrch() 

               

                  
    def autosrch(self):
        self.StudentsTabel.delete(*self.StudentsTabel.get_children())
        rollnumber = self.search.get()
        print(rollnumber)
        for val in db.validate(rollnumber):
            self.StudentsTabel.insert("",END , values=val)
            self.search.set("")
           # self.addbtn = Button(self.root, state = "disabled",command=self.addrec , text="ADD Details"   , image=self.add , compound=LEFT ,cursor="hand2", padx=5,activebackground="blue", font=("times",15,"bold") ,width=200, fg="white" , bg="blue" ).place(x=10,y=340)
      

    def save_xl(self):
        db.makecsv()   
        messagebox.showinfo("success","Record Saved Successfully in csv format" , parent = self.root)     
        
        



if __name__ == "__main__":
    root = Tk()
    obj = add_stds(root)
    obj.displayall()
    root.mainloop()
    

