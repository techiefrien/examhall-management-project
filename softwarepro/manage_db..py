import sqlite3


def database():
    con = sqlite3.connect(database="students.db")
    cur = con.cursor()
    sql="""
    
       CREATE TABLE IF NOT EXISTS stdtbl(

          sid INTEGER PRIMARY KEY AUTOINCREMENT,
          name text,
          roll text,
          department text,
          level text
       )
    
    
    
    
    """
    cur.execute(sql)
    con.commit()