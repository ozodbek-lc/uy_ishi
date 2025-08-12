def deco(func):
    def wrapper(*args, **kwargs):
        s=func(*args, **kwargs)
        return ''.join(s.replace(' ',''))
    return wrapper

@deco
def test():
    return "H e l l o"
print(test())
