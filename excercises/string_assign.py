name=input("enter your name:")
le=len(name)
sp=name.isalpha()
if le>=12 or  sp==False :
    print(f"{name} name is not valid...")
else:
    print(f"{name} is valid")
