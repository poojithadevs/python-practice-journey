from oop1 import car;

car1=car("BMW","alpina","white",2026,True)
car2=car("audi","audi R8","red",2025,False)

print("car1 details")
print(car1.brand)
print(car1.model)
print(car1.color)
print(car1.year)
print(car1.for_sale)
car1.drive()
car1.manufacture()

print("car2 details")
print(car2.brand)
print(car2.model)
print(car2.color)
print(car2.year)
print(car2.for_sale)
car2.drive()
car2.manufacture()
#class variable
print(car.name)