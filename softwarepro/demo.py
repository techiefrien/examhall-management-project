from codecs import namereplace_errors
from operator import index
from database_connection import std_database  , add_rooms , staff_database 
import pandas as pd

db = std_database("databases//students_data.db")
db1 = add_rooms("databases//rooms_details.db")
db2 = staff_database("databases//staff_data.db")

totalStudents =  db.counting()[0]



roomsperstd = int(input("Enter the number of  students per room :"))

dutycount  = totalStudents / roomsperstd

print(totalStudents)
print(roomsperstd)
a = int(dutycount)
print(a)
level1 = db2.staff_col()
level2 = db2.staff_col1()
level3 = db2.staff_col2()


print(level1)
print(level2)
print(level3)

staffcol1  = []
staffcol2 = []
staffcol3 = []
staffName = []
for i in range(len(level1)):
    staffName.append(level1[i][0])
    

    
for j in range(len(level2)):
    staffName.append(level2[j][0])




for k in range(len(level3)):
    staffName.append(level3[k][0])

"""


print(staffcol1)
print(staffcol2)
print(staffcol3)


a = int(dutycount)

div1 = a/2
div2 = a/3
div3 = a/5




range1 = int(div1)
val1OfNewList = staffcol1[0:range1]
for a in range(len(val1OfNewList)):
    staffName.append(val1OfNewList[a])


range2 = int(div2)
val2OfNewList = staffcol2[0:range2]
for b in range(len(val2OfNewList)):
    staffName.append(val2OfNewList[b])

range3 = int(div3)
val3OfNewList = staffcol3[0:range3]
for c in range(len(val3OfNewList)):
    staffName.append(val3OfNewList[c])

print("staffname selected")
print(staffName)
"""


indexOfStaffName = 0      




val  = db.namecol()
val1 = db.rollcol()
val2 = db1.blockcol()
val3 = db1.rnamecol()
val4 = db1.rcapcol()
indexofroom = 0
subrow = [1,2,3]
row = [1,2,3,4,5]
seat = [1,2]
namelist = []
rolllist = []
block = []
roomlist = []
Subrow = []
Row = []
Seat = []

indexofsubrow = 0
indexofrow = 0
indexofseat = 0
staffNameList = []

def fifteen():
    global  staffNameList , indexOfStaffName , val , val1 , val2 , val3 , val4 , roomsperstd  , indexofrow  , indexofseat , indexofsubrow, indexofroom , subrow , row , seat , namelist , rolllist , block , roomlist , Subrow , Row , Seat

    for i in range(10000000):
        
        
        if i == 0 or i == 1 :
            pass
        elif i%roomsperstd==0:
            indexofroom = indexofroom+1 
        if i == 1 or i == 0:
            pass

        if i == 0 :
            print("new record") 

        elif i%roomsperstd == 0:
            # print(tplenamelist)
            #print(namelist)
            indexofsubrow = 0
            print(staffNameList)
            data  = {
                "name":namelist,
                "Roll No": rolllist,
                "Block" : block,
                "Room" : roomlist,
                "Sub Row":Subrow,
                "Row": Row,
                "Seat": Seat,
                "Staff Name": staffNameList
             }
            final_ans = pd.DataFrame(data)
            print(final_ans)
        
            indexOfStaffName = indexOfStaffName + 1
            staffNameList = [] 
            namelist = []
            rolllist = []
            block = []
            roomlist = []
            Subrow = []
            Row = []
            Seat = []
        
            print("new record")                                     
      



        try:
            looplist = []
            loopval1 = val[i]
            
            nameval = loopval1[0]
            loopval3 = val1[i]
            rollval = loopval3[0]
            loopval2 = val2[indexofroom]
            blockval = loopval2[0]
            loopval4 = val3[indexofroom]
            roomval = loopval4[0]    
                
            looplist.append(loopval1)
            looplist.append(loopval3)
            looplist.append(loopval2)
            looplist.append(loopval4)
            looplist.append(subrow)
            looplist.append(row)
            looplist.append(seat)
        


            
            #rollval = loopval1[1]
            namelist.append(nameval)
            rolllist.append(rollval)
            block.append(blockval)
            roomlist.append(roomval)
            if i == 0 or i == 1 :
                pass
        
            elif i % 5 == 0:
                indexofsubrow = indexofsubrow + 1

            if  i%roomsperstd == 0 or indexofsubrow == 3:
                indexofsubrow = 0

           
               

            Subrow.append(subrow[indexofsubrow])
            
           
        
            if  i % 1 == 0:
                indexofrow = indexofrow + 1
            
                if i == 0 or  indexofrow == 5  :
                    indexofrow = 0
                    #print(indexofrow)

            
    
            Row.append(row[indexofrow])
            Seat.append(seat[indexofseat])

            staffNameList.append(staffName[indexOfStaffName])
            
        # rolllist.append(rollval)
    

        except:
            print("students data over")
            print(namelist)
            print(staffNameList)
            
            data  = {
                "name":namelist,
                "Roll NO" : rolllist,
                "block": block,
                "Room" : roomlist,
                "Sub Row":Subrow,
                "Row": Row,
                "Seat": Seat,
                "Staff Name": staffNameList
            }
            final_ans = pd.DataFrame(data)
            print(final_ans)
            
            staffName[indexOfStaffName]
            staffNameList = []            
            namelist = []
            rolllist = []
            block = []
            roomsperstd = []
            Subrow = []
            Row = []
            Seat = []
            break
                
        #indexofrow = indexofrow + 1
        #print(indexofrow)
    
    
        tplenamelist = tuple( namelist )
       
    
    
    #   for k in range(1):
            
#fifteen()  




def abovefifteen():
    global val, indexOfStaffName , staffNameList , staffName , val1 , val2 , val3 , val4 , roomsperstd  , indexofrow  , indexofseat , indexofsubrow, indexofroom , subrow , row , seat , namelist , rolllist , block , roomlist , Subrow , Row , Seat

    for i in range(10000000):
        if i == 0 or i == 1 :
            pass
        elif i%roomsperstd==0:
            indexofroom = indexofroom+1 
        if i == 1 or i == 0:
            pass

        if i == 0 :
            print("new record") 

        elif i%roomsperstd == 0:
            # print(tplenamelist)
            #print(namelist)
            indexofsubrow = 0
            data  = {
                "name":namelist,
                "Roll No": rolllist,
                "Block" : block,
                "Room" : roomlist,
                "Sub Row":Subrow,
                "Row": Row,
                "Seat": Seat,
                "Staff Name": staffNameList
             }
            final_ans = pd.DataFrame(data)
            print(final_ans)

            indexOfStaffName = indexOfStaffName +1
            staffNameList = []
            namelist = []
            rolllist = []
            block = []
            roomlist = []
            Subrow = []
            Row = []
            Seat = []
        
            print("new record")                                     
      



        try:
            looplist = []
            loopval1 = val[i]
            
            nameval = loopval1[0]
            loopval3 = val1[i]
            rollval = loopval3[0]
            loopval2 = val2[indexofroom]
            blockval = loopval2[0]
            loopval4 = val3[indexofroom]
            roomval = loopval4[0]    
                
            looplist.append(loopval1)
            looplist.append(loopval3)
            looplist.append(loopval2)
            looplist.append(loopval4)
            looplist.append(subrow)
            looplist.append(row)
            looplist.append(seat)
        


            
            #rollval = loopval1[1]
            namelist.append(nameval)
            rolllist.append(rollval)
            block.append(blockval)
            roomlist.append(roomval)
            

           
               

            
            
           
        
            if  i % 2 == 0:
                indexofrow = indexofrow + 1
            
            if i == 0 or  indexofrow == 5  :
                indexofrow = 0
                    #print(indexofrow)
            if i == 0 or i == 1 :
                pass
        
            elif i % 10 == 0:
                indexofsubrow = indexofsubrow + 1

            if  i%roomsperstd == 0 or indexofsubrow == 3:
                indexofsubrow = 0
           
            if i % 1 == 0 :
                indexofseat = indexofseat + 1

            if indexofseat == 2 or i == 0:
                indexofseat = 0
            # print(indexofseat)       
      
        
            
            Subrow.append(subrow[indexofsubrow])
            Row.append(row[indexofrow])
            Seat.append(seat[indexofseat])

            staffNameList.append(staffName[indexOfStaffName])
            
            # rolllist.append(rollval)
    

        except:
            print("students data over")
            #print(namelist)
            data  = {
                "name":namelist,
                "Roll NO" : rolllist,
                "block": block,
                "Room" : roomlist,
                "Sub Row": Subrow,
                "Row": Row,
                "Seat": Seat,
                  
            }
            final_ans = pd.DataFrame(data)
            print(final_ans)
            namelist = []
            rolllist = []
            block = []
            roomsperstd = []
            Subrow = []
            Row = []
            Seat = []
            break
                
        #indexofrow = indexofrow + 1
        #print(indexofrow)
    
    
        tplenamelist = tuple( namelist )
       

if roomsperstd < 15 :
    fifteen()    
else :    
    abovefifteen()