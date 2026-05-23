def add_veggies(func):
    def wrapper(*args,**kwargs):
        print("added veggies 🍅🫑🥕")
        func(*args,**kwargs)
    return wrapper

def add_corn(func):
    def wrapper(*args,**kwargs):
        print("added corn🌽")
        func(*args,**kwargs)
    return wrapper

def take_coke(fun):
    def coke(*args,**kwargs):
        print("take your coke🥤")
        fun(*args,**kwargs)
    return coke


@take_coke
@add_corn
@add_veggies
def get_burrito(type):
    print(f"here is your {type} burrito🌯")

get_burrito("chicken")