class Laptop():
    def __init__(self,name,price,storage):
        self.name=name
        self.price=price
        self.storage=storage
    def __str__(self):
        return f"name:{self.name} price:{self.price}  storage:{self.storage}"
    def __eq__(self,other):
        return self.name == other.name
    def __gt__(self,other):
        return self.price>other.price
    def __add__(self,other):
        return self.price+other.price
    def __contains__(self,key):
        return key in self.name 
    def __getitem__(self,key):
        if key=="name":
            return self.name
        elif key=="price":
            return self.price
        else:
            return self.storage
    #def __len__(self):
       # return len(self.name)

    
laptop1=Laptop("dell",60000,128)
laptop2=Laptop("mac",120000,256)
laptop3=Laptop("lenovo",100000,512)
print(laptop1)
print(laptop2)
print(laptop3)
print(laptop1==laptop2)
print(laptop2<laptop3)
print(laptop1<laptop2)
print(f"total price={laptop1+laptop2}")
print("l" in laptop1)
print(laptop2['name'])
print(len(laptop2))