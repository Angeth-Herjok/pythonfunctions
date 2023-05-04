from paramiko import Agent


class Student:
    name="Angeth"
    age=21
    school="AkiraChix"
    nationality="Kenyan"
    first_name="Becky"
    last_name="Herjok"
    country="Kenya"


    # constructor using self and __init__
# class Student:
#     school="AkiraChix"
#     def __init__(self,name,age,nationality):
#         self.name=name
#         self.age=age
#         self.nationality=nationality


# to create functions/objects inside class

class Student:
    school="AkiraChix"
    def __init__(self,name,age,nationality,first_name,last_name,country):
        self.name=name
        self.age=age
        self.nationality=nationality
        self.first_name=first_name
        self.last_name=last_name
        self.country=country
        
    def greet_student(self):
        return f"Hello {self.name},welcome to {self.school},proudly {self.nationality}"
    def show_full_name(self):
        return f"{self.first_name}  {self.last_name}"
    def year_of_birth(self):
        return f"{2023-{self.age}}"
    
    def show_initials(self):
        return f"{self.first_name[0].uppercase()} {self.last_name[0].uppercase()}"
        

     

# 1) Update the Student Class to include these attributes - first_name, last_name, age, country
#      - Add these methods to the Student class
#              - show_full_name
#              - year_of_birth
#              - show_initials



# 2) Create 3 files in the classes directory car.py, fruit.py, and bank.py. 
# Define the following classes in each module respectively. 
# Car
# Fruit
# Account
# Each class should have one class attribute and three instance variables.
