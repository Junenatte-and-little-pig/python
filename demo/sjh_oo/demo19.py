# -*- encoding: utf-8 -*-
from collections.abc import Iterable


class BasicClass(object):
    """
    this is a demo class to show basic functions from python
    """

    def __init__(self, b, a, s, i, c):
        self.b = b
        self.a = a
        self.s = s
        self.i = i
        self.c = c
        print("__init__:this is a constructor")

    def __call__(self):
        return "call by object"

    def __str__(self):
        """
        if this is not overrode, it will return
        the class family of the object and its id
        example:<__main__.BasicClass object at 0x000001D24C16EA88>
        """
        return self.b + self.a + self.s + self.i + self.c

    def __add__(self, other):
        """
        there of course are __sub__, __mul__, __truediv__, __divmod__, __mod__, __pow__ for overriding.
        these are for (BasicClass, other) operation,
        and functions with r prefix are for (other, BasicClass) operation,
        and functions with i prefix are for BasicClass operation= other, and will looking for basic functions if missing
        """
        return BasicClass(self.b + other.b, self.a + other.a, self.s + other.s,
                          self.i + other.i, self.c + other.c)

    # __getitem__, __setitem__, __delitem__ apply for index operation, and even slice
    def __getitem__(self, item):
        """
        item.start, item.stop, item.step for slice
        """
        return self.__dict__[item]

    def __setitem__(self, key, value):
        self.__dict__[key] = value

    def __delitem__(self, key):
        del self.__dict__[key]

    def __iter__(self):
        return iter([self.b, self.a, self.s, self.i, self.c])

    def __del__(self):
        print("__del__:bye bye")


bc = BasicClass("h", "e", "l", "l", "o")
print("__doc__:%s" % bc.__doc__)
print("__module__:%s" % bc.__module__)
print("__class__:%s" % bc.__class__)
print("__call__:%s" % bc())  # same as BasicClass(b, a, s, i, c)()
print("__str___:%s" % str(bc))
print("__dict__:%s" % BasicClass.__dict__)  # for class
print("__dict__:%s" % bc.__dict__)  # for object
bc += bc
print("__add_:%s" % str(bc))
print(bc["b"])
for p in bc:
    print(p)
print(isinstance(bc,Iterable))