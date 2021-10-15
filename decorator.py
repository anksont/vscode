def decorator2(func):
    def inner_func(a,b):
        print("inner code")
        return func(a,b)
    return inner_func

@decorator2
def divide(x,y):
    return x/y
@decorator2
def add(x,y):
    return x+y


print(divide(2,3))
print(add(1,2))