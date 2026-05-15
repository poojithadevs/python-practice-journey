p=0
r=0
t=0
while p<=0:
    p=float(input("enter principle amount:"))
    if(p<=0):
     print("principle cant be 0 or less")
while r<=0:
   r=int(input("enter rate of interest:"))
   if r<=0:
      print("rate cant be 0 or less")
while t<=0:
   t=int(input("enter time:"))
   if t<=0:
      print("time cant be 0 or less")
n=int(input("enter n: "))
a=p*pow((1+(r/n)),t)
print(f"amount=${a}")



