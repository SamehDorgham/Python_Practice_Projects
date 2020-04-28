
import mysql.connector

myconn = mysql.connector.connect(username = "root" , password = "1234" , host = "localhost" , database = "sameh") 

mycursor = myconn.cursor()
mycursor.execute("ALTER TABLE movies CHANGE language movielanguage varchar(20)")
myconn.commit()
print("done")