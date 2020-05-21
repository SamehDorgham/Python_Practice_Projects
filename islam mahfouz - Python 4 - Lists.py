
Sameh = ["Python" , "VB.Net" , "MySQL" , "SQL Server"]
Web = ["HTML","CSS","JavaScript"]

print(Sameh[0])
Sameh.extend(Web)
print(Sameh)
Sameh.append("WordPress")
print(Sameh)
Sameh.insert(2,"DB2")
print(Sameh)
Sameh.remove("DB2")
print(Sameh)
Web.clear()
print(Web)
print(Sameh.index("MySQL"))
print(Sameh.count("Python"))
Sameh.sort()
print(Sameh)
New_sameh = Sameh.copy() #Shallow Copy لا تتغير مع تغير الأصل
new_sameh1 = sameh # نسخة تتغير مع تغير الأأصل
print(New_sameh)






