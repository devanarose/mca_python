#!C:\Users\devan\AppData\Local\Microsoft\WindowsApps\python.exe

import cgi
import cgitb
import MySQLdb

cgitb.enable()
try: 
    mydb = MySQLdb.connect(host="localhost",user="root",password="",db="samplepyth")
    myCursor = mydb.cursor()
    
    form=cgi.FieldStorage()
    id=form.getvalue('id')
    name=form.getvalue('name')
    
    sql = "insert into user values(%s,%s)"
    myCursor.execute(sql,(id,name))
    mydb.commit()   
    print("content-type:text/html")
    print()
    
     
except Exception as e:
    print(e)