
import mysql.connector

myconn = mysql.connector.connect (
    username = "root" ,
    password = "1234" ,
    host = "localhost" ,
    database = "Sameh"    
)

mycursor = myconn.cursor()

mycursor.execute("CREATE TABLE books (title varchar(100) , author varchar(100) , size varchar(100))")

sql = "INSERT INTO books (title,author,size) values (%s,%s,%s)"
data = [
    ("vb.net 2017" , "mohamed hamdy ghanem" , "600") ,
    ("C#.net 2017" , "mohamed hamdy ghanem" , "600") ,
    ("ASP.net 2017" , "mohamed hamdy ghanem" , "600") ,
    ("Python 3" , "Sameh Dorgham" , "600") , 
       ]


mycursor.executemany(sql,data)
myconn.commit()

print("done")