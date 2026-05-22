class Employee():
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def Show_details(self):
        print(f"Name:{self.name}")
        print(f"Salary:{self.salary}")

class Developer(Employee):
    def Coding(self):
        print(f"developer {self.name} works on coding")
class Manager(Employee):
    def Manage_team(self):
        print(f"manager {self.name} manages the team ")

emp1=Developer("nani",100000)
emp2=Manager("pooja",5000000)
emp1.Show_details()
emp1.Coding()
emp2.Show_details()
emp2.Manage_team()
