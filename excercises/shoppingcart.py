items=[]
prices=[]
total=0

while True:
 item=input("entre item to buy(x to stop):")
 if item.lower()=="x":
  break
 else:
  price=float(input(f"enter price of {item}:"))
  items.append(item)
  prices.append(price)
  total+=price

print("----your cart----")
for a,b in zip(items,prices):
  print(f"{a} : ${b}")
print(f"total:{total}")
