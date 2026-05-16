def add_stu(*args,**kwargs):
    for arg in args:
        print(arg)
    for key,value in kwargs.items():
        print(f"{key}:{value}")
add_stu(101,
        "sara",
        "python",
        "math",
        "AI",
        age=19,
        city="hyd",
        cgpa=8.9
        )