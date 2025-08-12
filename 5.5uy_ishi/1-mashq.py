def deco(func):
    def wrapper(*args, **kwargs):
        s=func(*args, **kwargs)
        return ''.join(reversed(s))
    return wrapper

@deco
def test():
    return "Hello"
print(test())
