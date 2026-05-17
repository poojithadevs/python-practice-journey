import random

def spin():
    symbols=['🦋','🍑','🐧','🦈','🍗']
    return [random.choice(symbols) for _ in range(3)]

def row(spin_row):
    rows=[]
    rows.append(spin)
    return rows


def game(row,bet):
    if row[0]==row[1]==row[2]:
        if row[0]=='🦋':
            return bet*20
        elif row[0]=='🍑':
            return bet*30
        elif row[0]=='🐧':
            return bet*30
        elif row[0]=='🦈':
            return bet*30
        else :
            return bet*30
    else :
        return 0
    
is_running=True
balance=1000

while is_running:
    if balance==0:
            print("you finished your amount...")
            print("you cant play now")
            print("---THANK YOU💐---")
            break
    choice=input("do u wannna play (Y/n):")
    if choice=="n":
        break
    elif choice=='y':
        print(f"your current balance:${balance}")
        bet=int(input("place your bet:"))

        if bet>balance:
            print("insufficient balance you cant bet...")
            continue
    
        balance-=bet

        spin_row=spin()
        print(" ".join(spin_row))
        row(spin_row)

        get_balance=game(spin_row,bet)

        if get_balance > 0:
            print(f"yay!😍 you won ${get_balance}")
        else:
            print("oops😓 you lost...")
        
        balance+=get_balance
    else:
        print("choose correct option from (y/n)")
        continue
    
        

        
        
