

StudentInfo = {}

while True :
    
    StudentName = input("enter Student Name : ")
    
        
    if StudentName == "stop" :
        
        break
    
    else :        
       
       GPA = int(input("enter GPA : ")) 
        

    StudentInfo.update({StudentName:GPA})

MaxGPA =  max(StudentInfo.values())

print (MaxGPA)
