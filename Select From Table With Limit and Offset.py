
import mysql.connector

myconn = mysql.connector.connect( username = "root" , password = "1234" , host = "localhost" , database = "Sameh")

mycursor = myconn.cursor()

mycursor.execute("select * from movies LIMIT 4 OFFSET 3")

myresult = mycursor.fetchall()

print(myresult)  





