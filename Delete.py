
import mysql.connector

myconn = mysql.connector.connect(username = "root" , password = "1234" , host = "localhost" , database = "sameh") 

mycursor = myconn.cursor()
mycursor.execute("DELETE FROM movies WHERE moviename = 'Now You See Me'")
myconn.commit()
print("done")