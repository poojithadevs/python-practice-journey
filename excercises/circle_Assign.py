import math
r=float(input("enter radius of circle:"))
cir=2*(math.pi)*r
area=(math.pi)*pow(r,2)
print(f"area={round(area,1)}")
print(f"circumference:{round(cir,2)}")