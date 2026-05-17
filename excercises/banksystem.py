
def current_balance(total):
    print(f"your current balance:${total}")
def deposit():
    amount=int(input("enter amount to deposit:"))
    if amount<0:
        print("amount should be greater than 0")
        return 0
    else:
        print(f"${amount} deposited")
        return amount
def withdraw(total):
    amount=int(input("enter amount to withdraw:"))
    if amount>total:
        print(f"insufficient balance...")
        return 0
    elif amount<0:
        print("amount should be greater than 0")
        return 0
    else:
        print(f"${amount} withdrawed")
        return amount
    
def main():
    total=0
    running=True
    while running:
        print("************************************")
        print("--BANKING PROGRAM--")
        print("1.check balance\n 2.deposit\n 3.withdraw\n 4.exit")
        choice=input("enter your choice:")
        match choice:
            case "1":
                current_balance(total)
            case "2":
                total+=deposit()
            case "3":
                total-=withdraw(total)
            case "4":
                print("THANKYOU VISIT AGAIN!!")
                running=False

            case _:
                print("invalid option...")

if __name__=='__main__':
    main()

