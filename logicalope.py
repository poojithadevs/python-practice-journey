x=int(input("enter no:"))
if x%2==0 and x%3==0:
    print(f"{x} is divisible by 6")
else:
    print(f"{x} not divisible by 6")
if x>0 and x%2==0:
    print(f"{x} is divisible by 2")
else:
    print(f"{x} is not divisible by 2")
if x==2 or not x%2==0:
    print(f"{x} is odd number")
else:
    print(f"{x} is even number")

