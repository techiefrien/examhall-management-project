from database_connection import staff_database

db = staff_database("databases//staff_data.db")



level1 = db.staff_col()
level2 = db.staff_col1()
level3 = db.staff_col2()


print(level1)
print(level2)
print(level3)

staffcol1  = []
staffcol2 = []
staffcol3 = []

for i in range(len(level1)):
    staffcol1.append(level1[i][0])
    

    
for j in range(len(level2)):
    staffcol2.append(level2[j][0])




for k in range(len(level3)):
    staffcol3.append(level3[k][0])




print(staffcol1)
print(staffcol2)
print(staffcol3)


a = 2 

div1 = a/2
div2 = a/3
div3 = a/5

newlist = []


range1 = int(div1)
val1OfNewList = staffcol1[0:range1]
for a in range(len(val1OfNewList)):
    newlist.append(val1OfNewList[a])


range2 = int(div2)
val2OfNewList = staffcol2[0:range2]
for b in range(len(val2OfNewList)):
    newlist.append(val2OfNewList[b])

range3 = int(div3)
val3OfNewList = staffcol3[0:range3]
for c in range(len(val3OfNewList)):
    newlist.append(val3OfNewList[c])

print(newlist)