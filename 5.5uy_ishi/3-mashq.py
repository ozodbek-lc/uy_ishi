def deco(func):
    def wrapper(*args, **kwargs):
        s=func(*args, **kwargs)
        return ''.join(s.lower())
    return wrapper

def deco1(func):
    def wrapper(*args, **kwargs):
        s=func(*args, **kwargs)+'***'
        return s
    return wrapper

@deco
@deco1
def test():
    return "Hello"
print(test())
