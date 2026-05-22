class Person():
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display(self):
        print(f"Name:{self.name}")
        print(f"Age:{self.age}")

class Student(Person):
    def marks(self):
        print(f"{self.name} got 90 marks")

class Teacher(Person):
    def subject(self):
        print(f"{self.name} teaches computer science")

class Principal(Teacher):
    def teach(self):
        print(f"{self.name} is a principal")

person1=Student("pooja",19)
person2=Teacher("abhi",27)
person3=Principal("saroja",50)

person1.display()
person1.marks()
person2.display()
person2.subject()
person3.display()
person3.teach()