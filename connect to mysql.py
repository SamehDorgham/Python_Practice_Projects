
import mysql.connector

myconn = mysql.connector.connect(
     username = "root" , 
     password= "1234" , 
     host = "localhost" , 
     database = "Sameh"
     )

mycursor = myconn.cursor()
mycursor.execute("CREATE TABLE movies (moviename varchar(100), plot varchar(500))")

print ("table created successfuly")








    
