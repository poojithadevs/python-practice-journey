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
throws=[]  
total=0

no_of_dice=int(input("how many u wanna throw?:"))

for die in range(no_of_dice):
    throws.append(random.randint(1,6))

for die in range(no_of_dice):
    for lines in dice.get(throws[die]):
        print(lines)

for die in throws:
    total+=die
print(f"total={total}")
