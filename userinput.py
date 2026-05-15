name=input("enter your name:")
age=input("age?:")
age=int(age) #we need to typecast to perform on these interger since it is string
#or
temp=int(input("enter fav no:")) 
print(f"hlo {name}")
print(f"your age is {age}")
age+=5
temp+=2
print(f"your age after 5 years will be {age}")
print(f"u r fav no. by adding 2 is {temp}")
