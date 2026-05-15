import random
#print("\u25CF \u2500  \u2510 \u2502 \u2514 \u2518 \u250c")
#● ─  ┐ │ ┄ ┘ ┌
#● ─  ┐ │ └ ┘ ┌



dice={
        1:("┌──────────┐",
           "│          │",
           "│    ●     │",
           "│          │",
           "└──────────┘"  ),
        2:("┌──────────┐",
           "│ ●        │",
           "│          │",
           "│        ● │",
           "└──────────┘"  ),
        3:("┌──────────┐",
           "│ ●        │",
           "│    ●     │",
           "│         ●│",
           "└──────────┘"  ),
        4:("┌──────────┐",
           "│●        ●│",
           "│          │",
           "│●        ●│",
           "└──────────┘"  ),
        5:("┌──────────┐",
           "│●        ●│",
           "│     ●    │",
           "│ ●       ●│",
           "└──────────┘"  ),
        6:("┌──────────┐",
           "│   ●   ●  │",
           "│   ●   ●  │",
           "│   ●   ●  │",
           "└──────────┘"  ),

}     
play=True  
total=0
print("---DICE ROLLER GAME---")
while play:
 throw_dice=input("throw the dice(y/n):").lower()
 if throw_dice=="n":
    print("--THANKS FOR PLAYING--")
    break
 else:
    throws=random.randint(1,6)
    total+=throws
    for line in range(5):
       print(dice[throws][line])
    print(f"your score={total}")


