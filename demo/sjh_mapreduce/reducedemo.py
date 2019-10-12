# -*- encoding: utf-8 -*-
from functools import reduce

newlist = [x for x in range(1, 101)]
r1 = reduce(lambda x, y: x + y, newlist)


def my_reduce(*args):
    print(args)
    my_sum = 0
    my_sum += sum(args)
    return my_sum


r2 = reduce(my_reduce, newlist)
print(r2)
