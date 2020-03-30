import functools

def wrapper(f):
    @functools.wraps(f)
    def inner(*args,**kwargs):
        return f(*args,**kwargs)
    return inner


"""
1.执行wrpper
2.重新赋值
add = wrapper(add)
"""

@wrapper
def add(x,y):
    """

    :param x:
    :param y:
    :return:
    """
    return x+y

print(add.__name__) #inner
print(add.__doc__)