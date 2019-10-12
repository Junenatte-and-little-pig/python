# -*- encoding: utf-8 -*-
import functools

print(dir(functools))


def show(*args, **kwargs):
    print(args)
    print(kwargs)


show1 = functools.partial(show, 1, 2, 3) # 从左至右固定某些参数
show()
show1()
show1(name="zhangsan", age="18")
