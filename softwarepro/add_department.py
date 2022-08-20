from audioop import add
from cProfile import label
from email.mime import image
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from webbrowser import BackgroundBrowser
from PIL import ImageTk
from database_connection import add_dep

global o 

o = add_dep("databases//departments_data.db")


class add_departments:
    def __init__(self , root):
        self.root = root
        self.root.geometry("500x500+400+100")
        self.root.focus()
        self.root.resizable(False,False)
        
        #------------icons---------------------
        self.headicon = ImageTk.PhotoImage(file="icons/department2.png")
        self.add = ImageTk.PhotoImage(file="icons/add.png" )  
        self.upd = ImageTk.PhotoImage(file="icons/update.png" )  
        self.rem = ImageTk.PhotoImage(file="icons/delete.png" ) 
        self.clearicon = ImageTk.PhotoImage(file="icons/clear.png") 

       #-------------------variables--------------
        self.departmentname = StringVar()
       
       
        #----------------------labels-------------------------------
        
        self.headlabl = Label(self.root , text="Add Department"  , image=self.headicon , compound=LEFT , padx= 10, bg="grey" , fg="white" , font=("times new roman",20,"bold") ).pack(fill=X)
        

        #-----------------------------------frames---------------------------
        self.entry_frame = Frame(self.root ,  background="silver")
        self.entry_frame.place(x=0 , y=35 , width=500 , height= 250)
        
        self.output_frame = Frame(self.root ,  background="white")      
        self.output_frame.place(x=0 , y=250 , width=500 , height= 250) 
        
        #-----------------------entry frame components--------------
        self.nameofdep = Label(self.entry_frame , text="Department Name" , font=("goudy old style",15,"bold") , fg="black" , bg="silver")
        self.nameofdep.place(x=30 , y=60)

        self.department = Entry(self.entry_frame  , textvariable=self.departmentname, font=("times new roman",15 , "bold") , fg="black" , bg="white")
        self.department.place(x=30 , y = 100 , width=200 )

        self.addbtn = Button(self.entry_frame  ,state="active", command=self.insert , cursor="hand2" , bg="blue" , activebackground="blue" , image=self.add  , compound=LEFT , padx=10, text="Add Record" , font=(" sans-serif" , 15 , "bold") )
        self.addbtn.place(x=300 , y=20)

        self.updatebtn = Button(self.entry_frame   , state="disabled",command= self.update, cursor="hand2"  , bg="green" , activebackground="green" ,  image=self.upd ,compound=LEFT , padx=10 , text="Update Record" , font=(" sans-serif" , 15 , "bold") )
        self.updatebtn.place(x=300 , y=70)

        self.delbtn = Button(self.entry_frame    , state="disabled", command= self.delte, cursor="hand2"  , bg="red" , activebackground="red", image=self.rem  , compound=LEFT  , padx=10 , text="Delete Record" , font=(" sans-serif" , 15 , "bold") )
        self.delbtn.place(x=300 , y=120)

        self.clrbtn = Button(self.entry_frame  , command=self.clearll, text="Clear All"   , bg="orange" , activebackground="orange", image=self.clearicon , compound=LEFT , padx=10 , cursor="hand2", font=(" sans-serif" , 15 , "bold") )
        self.clrbtn.place(x=300 , y=170)


        #================================output frame components=============================
       
        scrollx = Scrollbar(self.output_frame ,   orient=HORIZONTAL)
        scrolly = Scrollbar(self.output_frame , orient=VERTICAL) 
        

        self.styles = ttk.Style()
        self.styles.configure("Treeview" , rowheight = 50 , font=("sans-serif",15) , Background="white" , foreground="black")
        self.styles.configure("Treeview.Heading" , font=("sans-serif",15,"bold"),foreground="white" , background="grey")
        self.department_table = ttk.Treeview(self.output_frame ,xscrollcommand=scrollx.set , yscrollcommand= scrolly.set , columns=('sid',"Names") )
        
        self.department_table.heading("sid",text="S.ID")
        self.department_table.heading("Names",text="Department Name")
        self.department_table["show"] = 'headings'
        self.department_table.column("sid",width=10)
        self.department_table.column("Names",width=280)

        scrollx.config(command= self.department_table.xview)
        scrolly.config(command=self.department_table.yview)
        scrollx.pack(side=BOTTOM , fill=X)
        scrolly.pack(side=RIGHT , fill=Y)
        self.department_table.bind("<ButtonRelease-1>",self.getData)        
        self.department_table.pack(fill=BOTH , expand=1)
        self.displayall()
        self.displayall()


  #----------------------sub functions--------------------
    def getData(self,event):
        currnet_row = self.department_table.focus()
        data =  self.department_table.item(currnet_row)     
        global rows 
        rows = data["values"]
        

        self.departmentname.set(rows[1])
        self.addbtn = Button(self.entry_frame  ,state="disabled", command=self.insert , cursor="hand2" , bg="blue" , activebackground="blue" , image=self.add  , compound=LEFT , padx=10, text="Add Record" , font=(" sans-serif" , 15 , "bold") )
        self.addbtn.place(x=300 , y=20)
        self.updatebtn = Button(self.entry_frame   , state="active",command= self.update, cursor="hand2"  , bg="green" , activebackground="green" ,  image=self.upd ,compound=LEFT , padx=10 , text="Update Record" , font=(" sans-serif" , 15 , "bold") )
        self.updatebtn.place(x=300 , y=70)

        self.delbtn = Button(self.entry_frame    , state="active", command= self.delte, cursor="hand2"  , bg="red" , activebackground="red", image=self.rem  , compound=LEFT  , padx=10 , text="Delete Record" , font=(" sans-serif" , 15 , "bold") )
        self.delbtn.place(x=300 , y=120)

        
   
    def displayall(self):
        self.department_table.delete(*self.department_table.get_children())  
        for row in o.fetch():
            self.department_table.insert("", END , values=row)
    
    def clearll(self):
        self.departmentname.set("") 
        

    def insert(self):
        if self.departmentname.get() == "":
            messagebox.showerror("error","please fill the detalis", parent=self.root)
        else:
            self.departmentval = self.departmentname.get().upper()    
            o.insert(self.departmentval)
            messagebox.showinfo("success","Record added successfully" , parent=self.root)
            self.displayall()
            self.clearll()

    def update(self):
        if self.departmentname.get() == "":
            messagebox.showerror("error","please select the record to update" , parent= self.root)
        else:    
            self.departmentval = self.departmentname.get().upper()    
            o.update(rows[0] , self.departmentval)
            messagebox.showinfo("success","Record updated successfully" , parent = self.root)
            self.displayall()
            self.clearll()
            self.addbtn = Button(self.entry_frame  ,state="active", command=self.insert , cursor="hand2" , bg="blue" , activebackground="blue" , image=self.add  , compound=LEFT , padx=10, text="Add Record" , font=(" sans-serif" , 15 , "bold") )
            self.addbtn.place(x=300 , y=20)
            self.updatebtn = Button(self.entry_frame   , state="disabled",command= self.update, cursor="hand2"  , bg="green" , activebackground="green" ,  image=self.upd ,compound=LEFT , padx=10 , text="Update Record" , font=(" sans-serif" , 15 , "bold") )
            self.updatebtn.place(x=300 , y=70)

            self.delbtn = Button(self.entry_frame    , state="disabled", command= self.delte, cursor="hand2"  , bg="red" , activebackground="red", image=self.rem  , compound=LEFT  , padx=10 , text="Delete Record" , font=(" sans-serif" , 15 , "bold") )
            self.delbtn.place(x=300 , y=120)
        
 
    def delte(self):
        if self.departmentname.get() =="":
            messagebox.showerror("error","please select the data to delete" , parent= self.root)
        else:
            o.remove(rows[0])
            self.displayall()
            self.clearll()
            messagebox.showinfo("deleted","record deleted successfuly" , parent=self.root)
            self.addbtn = Button(self.entry_frame  ,state="active", command=self.insert , cursor="hand2" , bg="blue" , activebackground="blue" , image=self.add  , compound=LEFT , padx=10, text="Add Record" , font=(" sans-serif" , 15 , "bold") )
            self.addbtn.place(x=300 , y=20)

            self.updatebtn = Button(self.entry_frame   , state="disabled",command= self.update, cursor="hand2"  , bg="green" , activebackground="green" ,  image=self.upd ,compound=LEFT , padx=10 , text="Update Record" , font=(" sans-serif" , 15 , "bold") )
            self.updatebtn.place(x=300 , y=70)


            self.delbtn = Button(self.entry_frame    , state="disabled", command= self.delte, cursor="hand2"  , bg="red" , activebackground="red", image=self.rem  , compound=LEFT  , padx=10 , text="Delete Record" , font=(" sans-serif" , 15 , "bold") )
            self.delbtn.place(x=300 , y=120)


if __name__ == "__main__":
    root = Tk()
    obj = add_departments(root)
    root.mainloop()

