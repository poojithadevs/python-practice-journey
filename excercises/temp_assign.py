unit=input("is temp in celcius or farenheit(c/f):")
temp=float(input("enter the temperature:"))
if unit=="c":
    print(f"temp in farenheit:{(temp*9)/5}")
elif unit=="f":
    x=round((temp-32)*(5/9),2)
    print(f"temp in celsius:{x}")