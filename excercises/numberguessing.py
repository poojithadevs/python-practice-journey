import random
low=1
high=300
ans=random.randint(low,high)
gu=0

print("---NUMBER GUESSING GAME---")
print(f"select your choice between {low}-{high}:")


while True:
    guess=input("enter your choice:")
    if guess.isdigit():
        guess=int(guess)
        gu+=1
        if guess<low or guess>high:
            print("number is out of range...")
            print(f"select between {low}-{high}")
        else:
         if guess<ans:
            print("too low choose another number")
         elif guess>ans:
            print("too high choose another number")
         else:
            print(f"yayy {guess}!! thats correct answer..")
            print(f"no. of guessess={gu}")
    else:
        print("invalid choice...")
        print(f"plz select between {low}-{high}:")