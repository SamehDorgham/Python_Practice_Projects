
import mysql.connector

myconn = mysql.connector.connect( username = "root" , password = "1234" , host = "localhost" , database = "Sameh")

mycursor = myconn.cursor()

sql = "INSERT INTO movies (moviename , plot) VALUES ( %s , %s )"
data = ("i saw what you see last summer" , "Scary movie")

mycursor.execute(sql , data)
myconn.commit()

print("rows inserted successfully")



