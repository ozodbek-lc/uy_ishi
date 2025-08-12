def deco(func):
    a = []
    def wrapper(*args):
        return f"{max(*args)}-listdagi eng katta son\n{min(*args)}-listdagi eng kichik son"
    return wrapper

@deco
def test(*args):
    return args

print(test(23, 5, 23, 5,2))
