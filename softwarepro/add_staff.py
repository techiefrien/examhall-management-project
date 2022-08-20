from email.errors import MessageError
from logging import exception
from multiprocessing.sharedctypes import Value
from tkinter import *
from turtle import width
from PIL import ImageTk 
from tkinter import ttk , messagebox
import sqlite3
from numpy import add
from database_connection import staff_database , add_dep
import sqlite3

global db

db = staff_database("databases//staff_data.db")
db1 = add_dep("databases//departments_data.db")

class add_staff:
    def __init__(self , root ):
        self.root = root
        self.root.state("zoomed")
        self.root.resizable(False , False)
        self.root.focus()      

        #------------cions load----------
        self.headicon = ImageTk.PhotoImage(file="icons/dstd.png" )
        self.clearicon = ImageTk.PhotoImage(file="icons/clear.png")
        self.searchicon = ImageTk.PhotoImage(file="icons/search.png" )
        self.headicon = ImageTk.PhotoImage(file="icons/dstaff.png" )
        self.bg = ImageTk.PhotoImage(file="icons/bg3.jpg" )  
        self.add = ImageTk.PhotoImage(file="icons/add.png" )  
        self.upd = ImageTk.PhotoImage(file="icons/update.png" )  
        self.rem = ImageTk.PhotoImage(file="icons/delete.png" )  
        self.xlsicon = ImageTk.PhotoImage(file="icons/xl.png")
         
       #------------------------heading------
        self.heading = Label(self.root , image= self.headicon,  padx=10,compound= LEFT,text="Manage Staff Details",font=('goudy old style',20,"bold"),bg="#b246ff",fg="black")
        self.heading.pack(fill=X)

      #------------------------variable---------------
        self.staff_name = StringVar()
        self.staff_roll = StringVar()
        self.staff_department = StringVar()
        self.staff_level = StringVar()  
        self.search = StringVar()
  
       #---------------frames-------
        self.input_frame = Frame(self.root , background="black" , height=350 , width = 1366 )
        self.input_frame.place(x=0 , y=50 )
        #self.output_frame = Frame(background="white" , height=350 , width = 1366 )
        #self.output_frame.place(x=0 , y=400 )

      #==============labels and inputfld in input frams================
        self.namelbl = Label(self.root , text="NAME" , font=("sans-serif",15,"bold"),fg="white",bg="black").place(x=100,y=100)
        self.rollnumlbl = Label(self.root , text="UNIQUE ID\n (Unique)" , font=("sans-serif",15,"bold"),fg="white",bg="black").place(x=700,y=100)
        self.departmentlbl = Label(self.root , text="DEPARTMENT" , font=("sans-serif",15,"bold"),fg="white",bg="black").place(x=100,y=200)
        self.yearlbl = Label(self.root , text="EXPERIECNCE" , font=("sans-serif",15,"bold"),fg="white",bg="black").place(x=660,y=200)
        
        val =  db1.list_items()
        val = tuple(val)
        


        self.nameentry = Entry(self.root , textvariable=self.staff_name,  width=20 , fg="black" , bd=5 , bg="white" , font=("goudy new style",19,"bold")).place(x=250 , y=100)
        self.rollnumentry = Entry(self.root  , textvariable=self.staff_roll, width=20 , fg="black" , bd=5 , bg="white" , font=("goudy new style",19,"bold")).place(x=900, y=100)
        self.staff_departments = ttk.Combobox(self.root ,state="Readonly", textvariable=self.staff_department , values= val  , font=("goudy new style",20,"bold")).place(x=250, y=200 , width = 300 , height=40 )
        self.year_list = ttk.Combobox(self.root ,textvariable=self.staff_level,  font=("goudy new style",20,"bold"), values= ("0-1 Year" , "1-4 Year" , "Above 4 Years" , "HOD") ).place(x=900 , y=200 , width=300)

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
        self.StudentsTabel.heading("levels",text="EXPERIENCE")
        self.StudentsTabel["show"] = 'headings'
        self.StudentsTabel.column("sid",width=10)
        self.StudentsTabel.column("names",width=280)
        self.StudentsTabel.column("rollnumber",width=200)
        self.StudentsTabel.column("department",width=200)
        self.StudentsTabel.column("levels",width=200)
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

        self.staff_name.set(rows[1])
        self.staff_roll.set(rows[2])
        self.staff_department.set(rows[3])
        self.staff_level.set(rows[4])
        self.addbtn = Button(self.root, state = "disabled",command=self.addrec , text="ADD Details"   , image=self.add , compound=LEFT ,cursor="hand2", padx=5,activebackground="blue", font=("times",15,"bold") ,width=200, fg="white" , bg="blue" ).place(x=10,y=340)
        self.updatebtn = Button(self.root ,command=self.updrec, state = "active", text="UPDATE Details" , font=("times",15,"bold") , cursor="hand2" ,  activebackground="green" ,width=200,image=self.upd , compound=LEFT , padx=5, fg="white" , bg="orange" ).place(x=250,y=340)
        self.deletebtn = Button(self.root ,command=self.deleterec, state = "active", text="DELETE Details" , font=("times",15,"bold"), cursor="hand2",activebackground='red',width=200,image=self.rem , compound=LEFT , padx=5, fg="white" , bg="red" ).place(x=490,y=340)
       
    
    def displayall(self):
        self.StudentsTabel.delete(*self.StudentsTabel.get_children())  
        for row in db.fetch():
            self.StudentsTabel.insert("", END , values=row)
        
  

    def clearall(self):
        
      self.staff_name.set("")
      self.staff_roll.set("")
      self.staff_department.set("")
      self.staff_level.set("")        

    def addrec(self):
        
      
        if self.staff_name.get()=="" or self.staff_roll.get()=="" or self.staff_department.get()=="" or self.staff_level.get()=="":
            messagebox.showerror('error',"please fill the all details" , parent = self.root)
            
        
        
        else:
            rollnum = self.staff_roll.get().upper()
            db.insert(self.staff_name.get(),rollnum,self.staff_department.get(), self.staff_level.get()) 
            self.displayall()         
            self.clearall()
            messagebox.showinfo("Success","Record Added Successfuly" , parent = self.root)

    def deleterec(self):
        if self.staff_name.get()=="" or self.staff_roll.get()=="" or self.staff_department.get()=="" or self.staff_level.get()=="":
            messagebox.showerror('error',"please Select the data to delete" , parent= self.root)
            
        else:  
            staff_database.remove(db,rows[0])
            self.displayall()         
            self.clearall()
            messagebox.showinfo("Success","Record deleted successfuly" , parent = self.root)
            self.addbtn = Button(self.root, state = "active",command=self.addrec , text="ADD Details"   , image=self.add , compound=LEFT ,cursor="hand2", padx=5,activebackground="blue", font=("times",15,"bold") ,width=200, fg="white" , bg="blue" ).place(x=10,y=340)
            self.updatebtn = Button(self.root ,command=self.updrec, state = "disabled", text="UPDATE Details" , font=("times",15,"bold") , cursor="hand2" ,  activebackground="green" ,width=200,image=self.upd , compound=LEFT , padx=5, fg="white" , bg="orange" ).place(x=250,y=340)
            self.deletebtn = Button(self.root ,command=self.deleterec, state = "disabled", text="DELETE Details" , font=("times",15,"bold"), cursor="hand2",activebackground='red',width=200,image=self.rem , compound=LEFT , padx=5, fg="white" , bg="red" ).place(x=490,y=340)
       

    def updrec(self):
        print(self.staff_name.get())
        print(self.staff_roll.get())
        print(self.staff_department.get())
        print(self.staff_level.get())
        if self.staff_name.get()=="" or self.staff_roll.get()=="" or self.staff_department.get()=="" or self.staff_level.get()=="":
            messagebox.showerror('error',"please select the data the record to update" , parent = self.root)  
            print(self.staff_name.get())
            print(self.staff_roll.get())
            print(self.staff_department.get())
            print(self.staff_level.get())
        
        else:
            rollnum = self.staff_roll.get().upper()
            db.update(rows[0],self.staff_name.get(),rollnum,self.staff_department.get(),self.staff_level.get()) 
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
            messagebox.showerror("errr","Reord not found",parent=self.root)
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
        try:
            db.makecsvs()   
            messagebox.showinfo("success","Record Saved Successfully in csv format" , parent = self.root)     
        except exception as ex:
            messagebox.showerror("error",f"There is error due to {str(ex)}")





if __name__ == "__main__":
    root = Tk()
    obj = add_staff(root)
    obj.displayall()
    root.mainloop()




