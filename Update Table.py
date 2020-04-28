
import mysql.connector

myconn = mysql.connector.connect(username = "root" , password = "1234" , host = "localhost" , database = "sameh") 

mycursor = myconn.cursor()
mycursor.execute("UPDATE movies SET movielanguage = 'English'")
myconn.commit()
print("done")