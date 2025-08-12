def deco(func):
    def wrapper(numbers):
        a = []
        for num in numbers:
            if num > 0 and num % 2 == 0:
                a.append(num)
        return func(a)
    return wrapper

@deco
def number(nums):
    return nums

nums = [-5, 0, 2, 7, 8, -4, 10, -1, 12]
print(number(nums))
