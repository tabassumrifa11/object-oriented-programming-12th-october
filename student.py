print("\033c")

class student:
    
     grade = 8
     print(f"I am a student of grade {grade}")
     
     def __init__(self, name, age):
         self.name = name
         self.age = age
         
         

rifa = student("Rifa", 14)
kashfia = student("Kashfia", 15)
junaira = student("Junaira", 12)


print(f"Name: {rifa.name}\nAge: {rifa.age}\n\n")
print(f"Name: {kashfia.name}\nAge: {kashfia.age}\n\n")
print(f"Name: {junaira.name}\nAge: {junaira.age}")


print(f"\n\nRifa Grade: {rifa.grade}")
print(f"\nKashfia Grade: {kashfia.grade}")
print(f"\nJunaira Grade: {junaira.grade}")