'''
def showSkills(*skills):
    for skill in skills:
        print(f"{skill}")

showSkills("python","html","MySQL","CSS") 
'''
       

def showSkills(** skills):
    for skill , value in skills.items():
        print(f"{skill} ==> {value}")

showSkills(python = "90%",mysql = "80%",html = "80%") 

       