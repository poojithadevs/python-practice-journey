import random
list=("rock","paper","scissors")
comp=random.choice(list)
user=input("enter choice (rock,paper,scissors):")

print(f"player:{user}")
print(f"computer:{comp}")

if user==comp:
    print("its a tie..")
elif user=="rock" and comp=="scissors":
    print("you won!!")
elif user=="paper" and comp=="rock":
    print("you won!!")
elif user=="scissors" and comp=="paper":
    print("you won!!")
else:
    print("computer won!! you lose...")



