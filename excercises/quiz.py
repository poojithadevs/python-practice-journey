questions=[["2*12=?"],
           ["3*12=?"],
           ["4*12=?"],
           ["5*12=?"],
          ]

answers=["a","b","c","d"]


options=[["a.24 b.36 c.48 d.60"],
         ["a.24,b.36 c.48 d.60"],
         ["a.24,b.36,c.48,d.60"],
         ["a.24,b.36,c.48,d.60"]]
score=0
        
for x,y,z in zip(questions,options,answers):
    print("------------------------------------------")
    print(x[0])
    print(y[0])
    guess=input("enter option:")
    if  guess!=str(z):
        print("incorrect...")
        print(f"correct answer-{z}")
        
    else:
        print("correct")
        score+=1
print(f"score:{score}")

  
