def deco(func):
    a = []
    def wrapper(*args):
        for i in args:
            if i%2==1:
                a.append(i)
            else:
                print(f"{i} toq son emas")
        return a
    return wrapper

@deco
def test(*args):
    return args

print(test(23, 5, 23, 5,2))
