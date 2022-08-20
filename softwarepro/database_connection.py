import sqlite3
import pandas as pd



class std_database:
    def __init__(self,db):
        self.con = sqlite3.connect(db)
        self.cur  = self.con.cursor()
        sql="""
         
         CREATE TABLE IF NOT EXISTS studentsdata(

             sid INTEGER PRIMARY KEY AUTOINCREMENT ,
             name text,
             roll text,
             department text ,
             level text 
         )
        
        """
        self.cur.execute(sql)
        self.con.commit()

    #insert data into std database
    def insert(self, name , roll , department , level):
        self.cur.execute("INSERT INTO studentsdata values(NULL,?,?,?,?)",
                    (name,roll,department,level))
        self.con.commit()
    #fetchall datas from database
    def fetch(self):
        self.cur.execute("select * from studentsdata order by roll asc")
        
        row = self.cur.fetchall()
        return row
    #delete datas from databse
    def remove(self,sid):
        self.cur.execute("delete from studentsdata where sid=?",(sid,))
        self.con.commit()

    #update data from database
    def update(self,sid,name,roll,department,level):
        self.cur.execute("update studentsdata set name=? , roll=? , department=? , level=? where sid=?",
                            (name,roll,department,level,sid))    
        self.con.commit()                    

    #===============validate fun
    def validate(self,rollS):
        self.cur.execute(f"SELECT * from studentsdata where roll LIKE '%{rollS}%' ")
        cols = self.cur.fetchall()
        return cols

                
    def makecsv(self):
        self.level_tabel = pd.read_sql_query("select * from studentsdata where level like 'II Year' AND department = 'BCA'"  ,  self.con  ) 
        self.outcome_table=pd.DataFrame(self.level_tabel)
        self.outcome_table.to_csv("excel_files//students//BCA//second_year_students_data.csv")
        self.level_tabel1 = pd.read_sql_query("select * from studentsdata where level  = 'I Year' AND department = 'BCA'"  ,  self.con  ) 
        self.outcome_table1=pd.DataFrame(self.level_tabel1)
        self.outcome_table1.to_csv("excel_files//students//BCA//first_year_students_data.csv")
        self.level_tabel2 = pd.read_sql_query("select * from studentsdata where level like 'III Year' AND department = 'BCA'"  ,  self.con  ) 
        self.outcome_table2=pd.DataFrame(self.level_tabel2)
        self.outcome_table2.to_csv("excel_files//students//BCA//third_year_students_data.csv")
         
         #--------------------------BBA--------------------

        self.BBAlevel_tabel = pd.read_sql_query("select * from studentsdata where level like 'II Year' AND department = 'BBA'"  ,  self.con  ) 
        self.BBAoutcome_table=pd.DataFrame(self.BBAlevel_tabel)
        self.BBAoutcome_table.to_csv("excel_files//students//BBA//second_year_students_data.csv")
        self.BBAlevel_tabel1 = pd.read_sql_query("select * from studentsdata where level  = 'I Year' AND department = 'BBA'"  ,  self.con  ) 
        self.BBAoutcome_table1=pd.DataFrame(self.BBAlevel_tabel1)
        self.BBAoutcome_table1.to_csv("excel_files//students//BBA//first_year_students_data.csv")
        self.BBAlevel_tabel2 = pd.read_sql_query("select * from studentsdata where level like 'III Year' AND department = 'BBA'"  ,  self.con  ) 
        self.BBAoutcome_table2=pd.DataFrame(self.BBAlevel_tabel2)
        self.BBAoutcome_table2.to_csv("excel_files//students//BBA//third_year_students_data.csv")
         
 
        #===================================B.COM=================

        self.BCOMlevel_tabel = pd.read_sql_query("select * from studentsdata where level like 'II Year' AND department = 'B.COM'"  ,  self.con  ) 
        self.BCOMoutcome_table=pd.DataFrame(self.BCOMlevel_tabel)
        self.BCOMoutcome_table.to_csv("excel_files//students//B.COM//second_year_students_data.csv")
        self.BCOMlevel_tabel1 = pd.read_sql_query("select * from studentsdata where level  = 'I Year' AND department = 'B.COM'"  ,  self.con  ) 
        self.BCOMoutcome_table1=pd.DataFrame(self.BCOMlevel_tabel1)
        self.BCOMoutcome_table1.to_csv("excel_files//students//B.COM//first_year_students_data.csv")
        self.BCOMlevel_tabel2 = pd.read_sql_query("select * from studentsdata where level like 'III Year' AND department = 'B.COM'"  ,  self.con  ) 
        self.BCOMoutcome_table2=pd.DataFrame(self.BCOMlevel_tabel2)
        self.BCOMoutcome_table2.to_csv("excel_files//students//B.COM//third_year_students_data.csv")
          
      #-----------------------------BA.TAMIL------------------------------

        self.BATAevel_tabel = pd.read_sql_query("select * from studentsdata where level like 'II Year' AND department = 'BA.TAMIL'"  ,  self.con  ) 
        self.BATAoutcome_table=pd.DataFrame(self.BATAevel_tabel)
        self.BATAoutcome_table.to_csv("excel_files//students//BA.TAMIL//second_year_students_data.csv")
        self.BATAlevel_tabel1 = pd.read_sql_query("select * from studentsdata where level  = 'I Year' AND department = 'BA.TAMIL'"  ,  self.con  ) 
        self.BATAoutcome_table1=pd.DataFrame(self.BATAlevel_tabel1)
        self.BATAoutcome_table1.to_csv("excel_files//students//BA.TAMIL//first_year_students_data.csv")
        self.BATAlevel_tabel2 = pd.read_sql_query("select * from studentsdata where level like 'III Year' AND department = 'BA.TAMIL'"  ,  self.con  ) 
        self.BATAoutcome_table2=pd.DataFrame(self.BATAlevel_tabel2)
        self.BATAoutcome_table2.to_csv("excel_files//students//BA.TAMIL//third_year_students_data.csv")
          
       #--------------------------BA.ENGLISH------------------------------
        self.BAENlevel_tabel = pd.read_sql_query("select * from studentsdata where level like 'II Year' AND department = 'BA.ENGLISH'"  ,  self.con  ) 
        self.BAENoutcome_table=pd.DataFrame(self.BAENlevel_tabel)
        self.BAENoutcome_table.to_csv("excel_files//students//BA.ENGLISH//second_year_students_data.csv")
        self.BAENlevel_tabel1 = pd.read_sql_query("select * from studentsdata where level  = 'I Year' AND department = 'BA.ENGLISH'"  ,  self.con  ) 
        self.BAENoutcome_table1=pd.DataFrame(self.BAENlevel_tabel1)
        self.BAENoutcome_table1.to_csv("excel_files//students//BA.ENGLISH//first_year_students_data.csv")
        self.BAENlevel_tabel2 = pd.read_sql_query("select * from studentsdata where level like 'III Year' AND department = 'ENGLISH'"  ,  self.con  ) 
        self.BAENoutcome_table2=pd.DataFrame(self.BAENlevel_tabel2)
        self.BAENoutcome_table2.to_csv("excel_files//students//BA.ENGLISH//third_year_students_data.csv")
             
       #-----------------------BA.SANSKRIT-------------------------------------
        
        self.BASAlevel_tabel = pd.read_sql_query("select * from studentsdata where level like 'II Year' AND department = 'BA.SANSKRIT'"  ,  self.con  ) 
        self.BASAoutcome_table=pd.DataFrame(self.BASAlevel_tabel)
        self.BASAoutcome_table.to_csv("excel_files//students//BA.SANSKRIT//second_year_students_data.csv")
        self.BASAlevel_tabel1 = pd.read_sql_query("select * from studentsdata where level  = 'I Year' AND department = 'BA.SANSKRIT'"  ,  self.con  ) 
        self.BASAoutcome_table1=pd.DataFrame(self.BASAlevel_tabel1)
        self.BASAoutcome_table1.to_csv("excel_files//students//BA.SANSKRIT//first_year_students_data.csv")
        self.BASAlevel_tabel2 = pd.read_sql_query("select * from studentsdata where level like 'III Year' AND department = 'BA.SANSKRIT'"  ,  self.con  ) 
        self.BASAoutcome_table2=pd.DataFrame(self.BASAlevel_tabel2)
        self.BASAoutcome_table2.to_csv("excel_files//students//BA.SANSKRIT//third_year_students_data.csv")
           
       #-------------------BSC.COMPUTER SCIENCE----------------------------
       
        self.BSCSlevel_tabel = pd.read_sql_query("select * from studentsdata where level like 'II Year' AND department = 'BSC.COMPUTER SCIENCE'"  ,  self.con  ) 
        self.BSCSoutcome_table=pd.DataFrame(self.BSCSlevel_tabel)
        self.BSCSoutcome_table.to_csv("excel_files//students//BSC.COMPUTER_SCIENCE//second_year_students_data.csv")
        self.BSCSlevel_tabel1 = pd.read_sql_query("select * from studentsdata where level  = 'I Year' AND department = 'BSC.COMPUTER SCIENCE'"  ,  self.con  ) 
        self.BSCSoutcome_table1=pd.DataFrame(self.BSCSlevel_tabel1)
        self.BSCSoutcome_table1.to_csv("excel_files//students//BSC.COMPUTER_SCIENCE//first_year_students_data.csv")
        self.BSCSlevel_tabel2 = pd.read_sql_query("select * from studentsdata where level like 'III Year' AND department = 'BSC.COMPUTER SCIENCE'"  ,  self.con  ) 
        self.BSCSoutcome_table2=pd.DataFrame(self.BSCSlevel_tabel2)
        self.BSCSoutcome_table2.to_csv("excel_files//students//BSC.COMPUTER_SCIENCE//third_year_students_data.csv")
         
       
    
    #--------------------------------BSC.MATHS----------------------------
    
        self.BSMAlevel_tabel = pd.read_sql_query("select * from studentsdata where level like 'II Year' AND department = 'BSC.MATHS'"  ,  self.con  ) 
        self.BSMAoutcome_table=pd.DataFrame(self.BSMAlevel_tabel)
        self.BSMAoutcome_table.to_csv("excel_files//students//BSC.MATHS//second_year_students_data.csv")
        self.BSMAlevel_tabel1 = pd.read_sql_query("select * from studentsdata where level  = 'I Year' AND department = 'BSC.MATHS'"  ,  self.con  ) 
        self.BSMAoutcome_table1=pd.DataFrame(self.BSMAlevel_tabel1)
        self.BSMAoutcome_table1.to_csv("excel_files//students//BSC.MATHS//first_year_students_data.csv")
        self.BSMAlevel_tabel2 = pd.read_sql_query("select * from studentsdata where level like 'III Year' AND department = 'BSC.MATHS'"  ,  self.con  ) 
        self.BSMAoutcome_table2=pd.DataFrame(self.BSMAlevel_tabel2)
        self.BSMAoutcome_table2.to_csv("excel_files//students//BSC.MATHS//third_year_students_data.csv")
         
    #-------------------------------------BCS.PHY-------------------------

        self.BSPHlevel_tabel = pd.read_sql_query("select * from studentsdata where level like 'II Year' AND department = 'BSC.PHYSICS'"  ,  self.con  ) 
        self.BSPHoutcome_table=pd.DataFrame(self.BSPHlevel_tabel)
        self.BSPHoutcome_table.to_csv("excel_files//students//BSC.PHYSICS//second_year_students_data.csv")
        self.BSPHlevel_tabel1 = pd.read_sql_query("select * from studentsdata where level  = 'I Year' AND department = 'BSC.PHYSICS'"  ,  self.con  ) 
        self.BSPHoutcome_table1=pd.DataFrame(self.BSPHlevel_tabel1)
        self.BSPHoutcome_table1.to_csv("excel_files//students//BSC.PHYSICS//first_year_students_data.csv")
        self.BSPHlevel_tabel2 = pd.read_sql_query("select * from studentsdata where level like 'III Year' AND department = 'BSC.PHYSICS'"  ,  self.con  ) 
        self.BSPHoutcome_table2=pd.DataFrame(self.BSPHlevel_tabel2)
        self.BSPHoutcome_table2.to_csv("excel_files//students//BSC.PHYSICS//third_year_students_data.csv")
          
    

    #-----------------------------BSC.CHEM--------------------------------

        self.BSCHlevel_tabel = pd.read_sql_query("select * from studentsdata where level like 'II Year' AND department = 'BSC.CHEMISTRY'"  ,  self.con  ) 
        self.BSCHoutcome_table=pd.DataFrame(self.BSCHlevel_tabel)
        self.BSCHoutcome_table.to_csv("excel_files//students//BSC.CHEMISTRY//second_year_students_data.csv")
        self.BSCHlevel_tabel1 = pd.read_sql_query("select * from studentsdata where level  = 'I Year' AND department = 'BSC.CHEMISTRY'"  ,  self.con  ) 
        self.BSCHoutcome_table1=pd.DataFrame(self.BSCHlevel_tabel1)
        self.BSCHoutcome_table1.to_csv("excel_files//students//BSC.CHEMISTRY//first_year_students_data.csv")
        self.BSCHlevel_tabel2 = pd.read_sql_query("select * from studentsdata where level like 'III Year' AND department = 'BSC.CHEMISTRY'"  ,  self.con  ) 
        self.BSCHoutcome_table2=pd.DataFrame(self.BSCHlevel_tabel2)
        self.BSCHoutcome_table2.to_csv("excel_files//students//BSC.CHEMISTRY//third_year_students_data.csv")
         

    #---------------------BIOTECHNOLOGY-------------------------------

        self.BITClevel_tabel = pd.read_sql_query("select * from studentsdata where level like 'II Year' AND department = 'BSC.BIOTECHNOLOGY'"  ,  self.con  ) 
        self.BITCoutcome_table=pd.DataFrame(self.BITClevel_tabel)
        self.BITCoutcome_table.to_csv("excel_files//students//BSC.BIOTECHNOLOGY//second_year_students_data.csv")
        self.BITClevel_tabel1 = pd.read_sql_query("select * from studentsdata where level  = 'I Year' AND department = 'BSC.BIOTECHNOLOGY'"  ,  self.con  ) 
        self.BITCoutcome_table1=pd.DataFrame(self.BITClevel_tabel1)
        self.BITCoutcome_table1.to_csv("excel_files//students//BSC.BIOTECHNOLOGY//first_year_students_data.csv")
        self.BITClevel_tabel2 = pd.read_sql_query("select * from studentsdata where level like 'III Year' AND department = 'BSC.BIOTECHNOLOGY'"  ,  self.con  ) 
        self.BITCoutcome_table2=pd.DataFrame(self.BITClevel_tabel2)
        self.BITCoutcome_table2.to_csv("excel_files//students//BSC.BIOTECHNOLOGY//third_year_students_data.csv")


    #--------------------------------BIOCHEMISTRY-----------------

        self.BICHlevel_tabel = pd.read_sql_query("select * from studentsdata where level like 'II Year' AND department = 'BSC.BIOCHEMISTRY'"  ,  self.con  ) 
        self.BICHoutcome_table=pd.DataFrame(self.BICHlevel_tabel)
        self.BICHoutcome_table.to_csv("excel_files//students//BSC.BIOCHEMISTRY//second_year_students_data.csv")
        self.BICHlevel_tabel1 = pd.read_sql_query("select * from studentsdata where level  = 'I Year' AND department = 'BSC.BIOCHEMISTRY'"  ,  self.con  ) 
        self.BICHoutcome_table1=pd.DataFrame(self.BICHlevel_tabel1)
        self.BICHoutcome_table1.to_csv("excel_files//students//BSC.BIOCHEMISTRY//first_year_students_data.csv")
        self.BICHlevel_tabel2 = pd.read_sql_query("select * from studentsdata where level like 'III Year' AND department = 'BSC.BIOCHEMISTRY'"  ,  self.con  ) 
        self.BICHoutcome_table2=pd.DataFrame(self.BICHlevel_tabel2)
        self.BICHoutcome_table2.to_csv("excel_files//students//BSC.BIOCHEMISTRY//third_year_students_data.csv")

    def namecol(self):
        self.cur.execute( "select name from studentsdata" )
        val =self.cur.fetchall()
        return val
    
    def rollcol(self):
        self.cur.execute("select roll from studentsdata")
        val1= self.cur.fetchall()
        return val1

    def name_roll(self):
        self.cur.execute("select name,roll from studentsdata")
        val2= self.cur.fetchall()
        return val2
    
    def counting(self):
        self.cur.execute("select count(roll) from studentsdata")
        val = self.cur.fetchall()
        return val[0]
          

class staff_database:
    global listsgal
    listsgal = []
    def __init__(self,db):
        self.con = sqlite3.connect(db)
        self.cur  = self.con.cursor()
        sqlq="""
         
         CREATE TABLE IF NOT EXISTS staffdata(

             sid INTEGER PRIMARY KEY AUTOINCREMENT ,
             name text,
             roll text,
             department text ,
             level text 
         )
        
        """ 
        self.cur.execute(sqlq)
        self.con.commit()

    #insert data into std database
    def insert(self, name , roll , department , level):
        self.cur.execute("INSERT INTO staffdata values(NULL,?,?,?,?)",
                    (name,roll,department,level))
        self.con.commit()
    #fetchall datas from database
    def fetch(self):
        self.cur.execute("select * from staffdata ORDER BY level")
        row = self.cur.fetchall()
        return row
    #delete datas from databse
    def remove(self,sid):
        self.cur.execute("delete from staffdata where sid=?",(sid,))
        self.con.commit()

    #update data from database
    def update(self,sid,name , roll ,department,level):
        self.cur.execute("update staffdata set name=?  , roll=? , department=? , level=? where sid=?",
                            (name , roll,department,level,sid))    

    def makecsvs(self):
        staff_tabel = pd.read_sql_query("select * from staffdata"  ,  self.con  ) 
        outcome_table_staff=pd.DataFrame(staff_tabel)
        outcome_table_staff.to_csv("excel_files//staff//staffs_data.csv")
         

    def validate(self,rollS):
        self.cur.execute(f"SELECT * from staffdata where roll LIKE '%{rollS}%' ")
        cols = self.cur.fetchall()
        return cols
    
    def counting(self):
        self.cur.execute("select count(roll) from staffdata")
        val = self.cur.fetchall()
        return val[0]

    def staff_col(self):
       
        self.cur.execute("select name from staffdata where level ='0-1 Year'")
        val = self.cur.fetchall()
        return val     
        

    def staff_col1(self):
        self.cur.execute("select name from staffdata where level ='1-4 Year'")
        val = self.cur.fetchall()    
        return val    

    def staff_col2(self):
        self.cur.execute("select name from staffdata where level = 'Above 4 Years'")
        val  = self.cur.fetchall()
        return val    
class add_dep:
    def __init__(self , db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        sql = """
        
        create table if not exists department(

            did INTEGER PRIMARY KEY AUTOINCREMENT ,
            dname text

        )
        
        
        """
        self.cur.execute(sql)
        self.con.commit()

    def insert(self,name):
        self.cur.execute("insert into department values(NULL, ?)" , (name,))
        self.con.commit()

    def fetch(self):
        self.cur.execute("select * from department order by dname")
        row=self.cur.fetchall()
        return row

    
    def update(self,id,name):
        self.cur.execute("update department set dname=? where did=? " , 
                                        (name, id))
        self.con.commit()

    def remove(self,id):
        self.cur.execute("delete from department where did=?",(id,))
        self.con.commit()    

    def list_items(self):
        self.cur.execute("select dname from department order by dname")
        val = self.cur.fetchall()
        return val   

    def counting(self):
        self.cur.execute("select count(dname) from department")
        val = self.cur.fetchall()
        return val[0]

"""o = staff_database("staff_data.db")
o.makecsvs()  """

class add_rooms:
    def __init__(self,db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        query = """
        
        create table if not exists rooms1(
          rid INTEGER PRIMARY KEY AUTOINCREMENT , 
          rname text ,
          block text , 
          rcap integer 
          ) 
         
        
        """
        self.cur.execute(query)
        self.con.commit()
    
      

    def insert(self, name , block , rcap):
        self.cur.execute("INSERT INTO rooms1 values(NULL,?,?,?)",
                    (name,block,rcap))
        self.con.commit()                                                                                                                                                                                  
    
    
    def fetch(self):
        self.cur.execute("select * from rooms1")
        row = self.cur.fetchall()
        return row
        #print(row)
    
    def update(self ,id, name , blocks , rcap):
        self.cur.execute("update rooms1 set rname=? , block=? , rcap=? where rid=?" , 
                                             (name,blocks,rcap,id)) 
        self.con.commit()
       

    def remove(self,id):
        self.cur.execute("delete from rooms1 where rid=?",(id,))
        self.con.commit()

    def search(self,option,name):
        self.cur.execute(f"select * from rooms1 where {option} like '{name}'")
        val = self.cur.fetchall()
        return val

    def blockcol(self):
        self.cur.execute("select block  from rooms1")
        val = self.cur.fetchall()
        return val

    def rnamecol(self):
        self.cur.execute("select rname  from rooms1")
        val = self.cur.fetchall()
        return val

    def rcapcol(self):
        self.cur.execute("select rcap  from rooms1")
        val = self.cur.fetchall()
        return val

    def counting(self):
        self.cur.execute("select count(rname) from rooms1")
        val = self.cur.fetchall()
        return val[0]    

"""rmdb = add_rooms("databases//rooms_details.db")
rmdb.insert("p16","p-block",50)
rmdb.fetch()"""

#db = std_database("databases//students_data.db")
