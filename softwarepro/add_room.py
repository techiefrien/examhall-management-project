from os import access
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from setuptools import Command
from database_connection import add_rooms
from PIL import ImageTk

global db 

db4 = add_rooms("databases//rooms_details.db")

class  rooms:
    def __init__(self , root):
        self.root = root
        self.root.geometry("900x650+250+20")
        self.root.config(background = "white")
        self.root.resizable(False , False)

#===================================================================
#-----------------------------load icons----------------------------
        self.headicon = ImageTk.PhotoImage(file="icons//rooms.png")
        self.clearicon = ImageTk.PhotoImage(file="icons/clear.png")
        self.searchicon = ImageTk.PhotoImage(file="icons/search.png" )  
        self.add = ImageTk.PhotoImage(file="icons/add.png" )  
        self.upd = ImageTk.PhotoImage(file="icons/update.png" )  
        self.rem = ImageTk.PhotoImage(file="icons/delete.png" )  

#===========================================================
#----------------------------variables----------------------------

        self.room_name = StringVar() 
        self.block_name = StringVar()
        self.room_cap = StringVar()
        self.search_feild =  StringVar()
        self.searchby = StringVar()

#==============================================================
#----------------------------heding part ------------------

        self.heading  = Label(self.root  , image=self.headicon , compound=LEFT , padx=10, text="Manage Room details" , bg= "#847583" , fg='white' , font=("italic",19,"bold"))
        self.heading.pack(fill=X)

#=====================================================
#------------------data frames-----------------------
         
        self.dataframe = Frame(self.root , bg="black")
        self.dataframe.place(x=0 , y = 55 , width=900 , height=300)

        self.rname = Label(self.dataframe , text="Rooms Name" , fg="white" , bg="black" , font=('goudy old style',15,"bold") )
        self.rname.place(x=20 , y=70)

        self.rblock = Label(self.dataframe , text="Block Name" , fg="white" , bg="black" , font=('goudy old style',15,"bold") )
        self.rblock.place(x=20 , y=130)

        self.rcap = Label(self.dataframe , text="Rooms Capacity" , fg="white" , bg="black" , font=('goudy old style',15,"bold") )
        self.rcap.place(x=20 , y=190)

        self.rname_entry = Entry(self.dataframe  , textvariable=self.room_name, font=("",15,"bold") , bg="white" , fg="black") 
        self.rname_entry.place(x=180 , y=70)

        self.rblock_entry = Entry(self.dataframe , textvariable=self.block_name, font=("",15,"bold") , bg="white" , fg="black") 
        self.rblock_entry.place(x=180 , y=130)

        self.rname_entry = Entry(self.dataframe ,textvariable=self.room_cap, font=("",15,"bold") , bg="white" , fg="black") 
        self.rname_entry.place(x=180 , y=190)
        
        self.srclbl = Label(self.dataframe , text="Search By" , fg="white" , bg="black" , font=('goudy old style',10,"bold") )
        self.srclbl.place(x=40 , y=240)


        self.src = ttk.Combobox(self.dataframe ,textvariable=self.searchby, values=("Room Name","Block Name") , state="readonly" )
        self.src.set("Room Name")
        self.src.place(x=30 , y=265)
        
        self.searchentry = Entry(self.dataframe  ,textvariable=self.search_feild, width=20 , fg="black" , bd=5 , bg="white" , font=("goudy new style",15,"bold")).place(x=190,y=250)
        self.srchbtn = Button(self.dataframe , command=self.searchfrmdb , image=self.searchicon , bg="blue" )
        self.srchbtn.place(x=425 , y=250)



#======================================================================================
# -----------------------------------button frames--------------------------------------

        self.btnframes = Frame(self.dataframe  , bd=12  , relief=GROOVE , bg='grey')
        self.btnframes.place(x=480 , y=20 ,width=400 , height=230) 

        self.addbtn = Button(self.btnframes ,command=self.addrec, bd=8,relief=RAISED, state = "active", text="ADD Details"   , image=self.add , compound=LEFT ,cursor="hand2", padx=5,activebackground="blue", font=("times",15,"bold") ,width=200, fg="white" , bg="blue" ).place(x=70,y=10)
        self.updatebtn = Button(self.btnframes ,state="disabled", command= self.updrec ,bd=8,relief=RAISED,  text="UPDATE Details" , font=("times",15,"bold") , cursor="hand2" ,  activebackground="green" ,width=200,image=self.upd , compound=LEFT , padx=5, fg="white" , bg="green" ).place(x=70,y=60)
        self.deletebtn = Button(self.btnframes ,state="disabled", command=self.deleterec ,bd=8,relief=RAISED,  text="DELETE Details" , font=("times",15,"bold"), cursor="hand2",activebackground='red',width=200,image=self.rem , compound=LEFT , padx=5, fg="white" , bg="red" ).place(x=70,y=110)
        self.clearbtn = Button(self.btnframes , command=self.cleartxtfld ,bd=8,relief=RAISED, text="CLEAR Details" , image=self.clearicon, compound=LEFT, font=("times",15,"bold"),width=200 , cursor="hand2", activebackground="orange", padx=5 ,fg="white" , bg="orange" ).place(x=70,y=160)


#=================================================framee - 2 ======================================
#-------------------------------------data tables--------------------------------------------------

        self.datatable_frame = Frame(self.root , background="white" )
        self.datatable_frame.place(x=0 ,y = 355 , width=900 , height=300 )

        scrollx = Scrollbar(self.datatable_frame ,   orient=HORIZONTAL)
        scrolly = Scrollbar(self.datatable_frame, orient=VERTICAL)
       
        self.style = ttk.Style()
        self.style.configure("mystyle.Treeview" , rowheight = 50 , font=("sans-serif",15) , bg="white" , fg="black")
        self.style.configure("mystyle.Treeview.Heading" , font=("sans-serif",15,"bold"),fg="black" , bg="white")
        self.roomsTabel = ttk.Treeview(self.datatable_frame ,xscrollcommand=scrollx.set , yscrollcommand= scrolly.set , columns=('sid',"names","rollnumber" , "department" ) , style="mystyle.Treeview")
        
        self.roomsTabel.heading("sid",text="S.ID")
        self.roomsTabel.heading("names",text="Room NAME")
        self.roomsTabel.heading("rollnumber",text="Block Name")
        self.roomsTabel.heading("department",text="Room Capacity")
        self.roomsTabel["show"] = 'headings'
        self.roomsTabel.column("sid",width=50)
        self.roomsTabel.column("names",width=280)
        self.roomsTabel.column("rollnumber",width=200)
        self.roomsTabel.column("department",width=200)
        self.roomsTabel.bind("<ButtonRelease-1>",self.getData)
        scrollx.config(command= self.roomsTabel.xview)
        scrolly.config(command=self.roomsTabel.yview)
        scrollx.pack(side=BOTTOM , fill=X)
        scrolly.pack(side=RIGHT , fill=Y)
        
        self.roomsTabel.pack(fill=BOTH , expand=1)
        self.displayall()
        
        
#======================================================================
#-----------------------------sub functions---------------
    
    def getData(self,event):
        currnet_row = self.roomsTabel.focus()
        data =  self.roomsTabel.item(currnet_row)     
        global rows 
        rows = data["values"]

        self.room_name.set(rows[1])
        self.block_name.set(rows[2])
        self.room_cap.set(rows[3])
        self.addbtn = Button(self.btnframes ,command=self.addrec, bd=8,relief=RAISED, state = "disabled", text="ADD Details"   , image=self.add , compound=LEFT ,cursor="hand2", padx=5,activebackground="blue", font=("times",15,"bold") ,width=200, fg="white" , bg="blue" ).place(x=70,y=10)
        self.updatebtn = Button(self.btnframes ,state="active", command= self.updrec ,bd=8,relief=RAISED,  text="UPDATE Details" , font=("times",15,"bold") , cursor="hand2" ,  activebackground="green" ,width=200,image=self.upd , compound=LEFT , padx=5, fg="white" , bg="green" ).place(x=70,y=60)
        self.deletebtn = Button(self.btnframes ,state="active", command=self.deleterec ,bd=8,relief=RAISED,  text="DELETE Details" , font=("times",15,"bold"), cursor="hand2",activebackground='red',width=200,image=self.rem , compound=LEFT , padx=5, fg="white" , bg="red" ).place(x=70,y=110)
        
    
    
    def addrec(self):
        if self.room_name.get() =="" or self.block_name.get() == "" or self.room_cap.get() == "":
            messagebox.showerror("error","please fil the3 all details",parent=self.root)
        else:
            room_name = self.room_name.get().upper()
            block_name = self.block_name.get().upper()
            room_cap = self.room_cap.get()
            int(room_cap)
            db4.insert(room_name , block_name , room_cap)
            messagebox.showinfo("success","record added sucessfully" , parent=self.root)
            self.displayall()
            self.cleartxtfld()

    def displayall(self):
        self.roomsTabel.delete(*self.roomsTabel.get_children())  
        for row in db4.fetch():
            self.roomsTabel.insert("", END , values=row)
            
    def updrec(self):
        if self.room_name.get() =="" or self.block_name.get() == "" or self.room_cap.get() == "":
            messagebox.showerror("error","please fil the3 all details",parent=self.root)
        else:
            room_name1 = self.room_name.get().upper()
            block_name1 = self.block_name.get().upper()
            room_cap1 = self.room_cap.get()
            int(room_cap1)
            db4.update(rows[0],room_name1 , block_name1 , room_cap1)
            messagebox.showinfo("success","record updated sucessfully" , parent=self.root)
            self.displayall()
            self.cleartxtfld()
            self.addbtn = Button(self.btnframes ,command=self.addrec, bd=8,relief=RAISED, state = "active", text="ADD Details"   , image=self.add , compound=LEFT ,cursor="hand2", padx=5,activebackground="blue", font=("times",15,"bold") ,width=200, fg="white" , bg="blue" ).place(x=70,y=10)
            self.updatebtn = Button(self.btnframes ,state="disabled", command= self.updrec ,bd=8,relief=RAISED,  text="UPDATE Details" , font=("times",15,"bold") , cursor="hand2" ,  activebackground="green" ,width=200,image=self.upd , compound=LEFT , padx=5, fg="white" , bg="green" ).place(x=70,y=60)
            self.deletebtn = Button(self.btnframes ,state="disabled", command=self.deleterec ,bd=8,relief=RAISED,  text="DELETE Details" , font=("times",15,"bold"), cursor="hand2",activebackground='red',width=200,image=self.rem , compound=LEFT , padx=5, fg="white" , bg="red" ).place(x=70,y=110)
        

             
    def cleartxtfld(self):
        self.room_name.set("")
        self.room_cap.set("")
        self.block_name.set("")

    def deleterec(self):
        db4.remove(rows[0])
        messagebox.showinfo('success',"record deleted successfully" , parent=self.root)
        self.displayall()
        self.cleartxtfld()
        self.addbtn = Button(self.btnframes ,command=self.addrec, bd=8,relief=RAISED, state = "active", text="ADD Details"   , image=self.add , compound=LEFT ,cursor="hand2", padx=5,activebackground="blue", font=("times",15,"bold") ,width=200, fg="white" , bg="blue" ).place(x=70,y=10)
        self.updatebtn = Button(self.btnframes ,state="disabled", command= self.updrec ,bd=8,relief=RAISED,  text="UPDATE Details" , font=("times",15,"bold") , cursor="hand2" ,  activebackground="green" ,width=200,image=self.upd , compound=LEFT , padx=5, fg="white" , bg="green" ).place(x=70,y=60)
        self.deletebtn = Button(self.btnframes ,state="disabled", command=self.deleterec ,bd=8,relief=RAISED,  text="DELETE Details" , font=("times",15,"bold"), cursor="hand2",activebackground='red',width=200,image=self.rem , compound=LEFT , padx=5, fg="white" , bg="red" ).place(x=70,y=110)
        
    def searchfrmdb(self):
        if self.searchby.get() == "Room Name":
            self.srcby=self.searchby.get().replace("Room Name","rname")
        elif self.searchby.get() == "Block Name":
            self.srcby = self.searchby.get().replace("Block Name","block")

        search=self.search_feild.get().upper()   
        if self.search_feild.get() =="": 
            messagebox.showerror('error',"please fill the all details" , parent = self.root)
        elif  db4.search(self.srcby,search)==[]:
            messagebox.showerror('error',"Record not found",parent=self.root)
           
        else:    
            self.roomsTabel.delete(*self.roomsTabel.get_children())
            for col in db4.search(self.srcby,search):
                self.roomsTabel.insert("",END,values=col)
                self.search_feild.set("")



if __name__ == "__main__":
    root = Tk()
    object = rooms(root)
    object.displayall()
    root.mainloop()    
