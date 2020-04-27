
import mysql.connector

myconn = mysql.connector.connect( username = "root" , password = "1234" , host = "localhost" , database = "Sameh")

mycursor = myconn.cursor()

sql = "select * from movies where moviename = %s "
data = ('x-files',)

mycursor.execute(sql , data)

myresult = mycursor.fetchall()

print(myresult)  





