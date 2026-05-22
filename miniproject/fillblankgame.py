import random

letters=["audi","ferari","lamborgini","tata","toyota","rollsroys","mercedes"]

ran=random.choice(letters)
print(ran)

wrong_art={0:("o"),
           1:("o"
              "|"),
          2:("o"
            "/|\\"),
           3:("o"
             "/|\\"
             "/|") ,
         4:( "o"
            "/|\\"
            "/|\\")}
def wrong_ans():
 pass
def correct_ans():
 pass

is_running=True


def main():
 while is_running:
  guess=input("enter the letter of the word:")
  if guess!=ran:
   print
