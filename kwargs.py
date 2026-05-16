def address(**lists):
    for key in lists.keys():
        print(key)

    for value in lists.values():
        print(value)
        
    for x,y in lists.items():
        print(f"{x}:{y}")

address(vlg="kokapet",
        mdl="gandipet",
        city="hyd",
        state="telangana")
