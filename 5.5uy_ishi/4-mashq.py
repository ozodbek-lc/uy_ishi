def deco(func):
    a = []
    def wrapper(*args):
        for i in args:
            a.append(i)
        s = 1
        for son in a:
            s *= son
        return s
    return wrapper

@deco
def test(*args):
    return args

print(test(23, 5, 23, 5))
