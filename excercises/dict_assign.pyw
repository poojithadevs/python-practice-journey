food={"biryani":900,
      "kabad":300,
      "chicken 65":500,
      "mutton fry":600,
      "chilli chicken":700,
      "chapathi":50,
      "pulao":200,
      "manchurya":400,
      "coke":50}
cart=[]
total=0
print("------------menu-------------")
for x,y in food.items():
    print(f"{x:10}:${y}")

while True:
 order=input("enter your choice(q to quite):").lower()
 if order == "q":
    break
 elif food.get(order) !=None:
    cart.append(order)
for foods in cart:
   total+=food.get(foods)
print("---your order---")
for  a in cart():
   print(a)

print(f"total bill:{total}")
 
 

