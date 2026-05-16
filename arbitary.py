#no need to limit the arguments
#*args
def sum(*nums):
    total=0
    for num in nums:
        total+=num
    return total
print(sum(1,2,56))
print(sum(1,2))
print(sum(1))
print(sum(1,23,56,11,34,56))

def name(*args):
    for arg in args:
        print(arg,end=" ")
name("g","poojitha","yadav")