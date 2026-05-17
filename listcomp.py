num=[x*4 for x in range(1,10)]
num1=[x*x for x in range(1,10)]
print(num)
print(f"squares(1-10):{num1}")

list=[1,2,3,4,5,6,7,8,9,10]
even=[num for num in list if num%2==0]
odd=[num for num in list if num%2!=0]
pass_val=[num for num in list if num>5]
print(even)
print(odd)
print(pass_val)

names=["poojitha","aadi"]
new_name=[name.capitalize() for name in names]
print(new_name)