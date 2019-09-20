# -*- encoding: utf-8 -*-


def add1(a, b):
    su = a + b
    print(su)


def add2(a, b):
    su = a + b
    return su


def add3(a=1, b=2):
    su = a + b
    return su


def add4(*args):  # number是元组
    return sum(args)


def add5(**kwargs):  # number是字典
    return sum(kwargs.values())


def add6(*args, **kwargs):
    return sum(args), sum(kwargs.values())


# 匿名函数 适用于简单代码
add7 = lambda a, b: a + b


def add8(a, b, lam):
    """
    :type lam:lambda expression
    """
    return a, b, lam(a, b)


add1(1, 2)
a = 1
b = 2
add1(a, b)
add1(b=3, a=4)
print(add2(a, b))
print(add3())
print(add3(3))
print(add3(b=5))
print(add3(a, b))
print(add4(1, 2, 3, 4, 5))
print(add4(*(1, 2, 3, 4, 5)))
print(add5(a1=12, a2=23, a3=1))
print(add5(**{'a1': 12, 'a2': 23, 'a3': 1}))
print(add6(*(1, 2, 3, 4, 5), **{'a1': 12, 'a2': 23, 'a3': 1}))
print(add7(12, 20))
print(add8(12, 32, lambda x, y: x + y))
