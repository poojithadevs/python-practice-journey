def oprations():
    operator=input("enter the oprator:")
    match operator:
        case "+"|"-"|"*"|"/"|"%":

            a=int(input("enter a:"))
            b=int(input("enter b:"))
            match operator:
                case "+":
                    return a+b
                case "-":
                    return a-b
                case "*":
                    return a*b
                case "/":
                    return a/b
                case "%":
                    return a%b
        case _:
            return "not valid..."
print(oprations())
 
