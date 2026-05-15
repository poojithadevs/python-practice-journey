wt=float(input("enter your weight:"))
unit=input("conversion type kilo or pounds(k/p):")
if unit=="k":
    wt=wt*2.03
    u="kilos"
elif unit=="p":
    wt=wt/2.03
    u="pounds"
else:
    print("not valid")
print(f"your weight is:{round(wt,2)} {u}")