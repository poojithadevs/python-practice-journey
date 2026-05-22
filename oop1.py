class car:
 name="pooja"
 def __init__(self,brand,model,color,year,for_sale):
  self.brand=brand
  self.model=model
  self.color=color
  self.year=year
  self.for_sale=for_sale

 def drive(self):
  print(f"you can drive the {self.brand} {self.model}")

 def manufacture(self):
  print(f"the {self.brand} {self.model} is made in japan")
  