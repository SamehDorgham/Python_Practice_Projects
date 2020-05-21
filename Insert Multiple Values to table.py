
import mysql.connector

myconn = mysql.connector.connect( username = "root" , password= "1234" , host = "localhost" , database = "Sameh")

mycursor = myconn.cursor()

sql = "INSERT INTO movies(moviename , plot) VALUES (%s , %s)"
data = [
    ("Harry Potter" , "Adventure Movie") ,
    ("X-Files" , "Series") ,
    ("Dr.House" , "series") 
    ]

mycursor.executemany(sql , data)
myconn.commit()

print ("data inserted successfully")
print(mycursor.rowcount)

