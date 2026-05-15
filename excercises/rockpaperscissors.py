import random
list=("rock","paper","scissors","q")
play=True


while play:
  comp=random.choice(list)
  user=input("enter choice (rock,paper,scissors) q for quit:")
  if user not in list:
   print("enter correct option")
  else:
   if user=="q":
     print("THANK YOU")
     play= False
     break
   else:
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



