# -*- encoding: utf-8 -*-
class UpperAttrMetaClass(type):
    def __new__(mcs, future_class_name, future_class_parents,
                future_class_attr):
        new_attr = {}
        for name, value in future_class_attr.items():
            if not name.startswith("__"):
                new_attr[name.upper()] = value
        return super(UpperAttrMetaClass, mcs).__new__(mcs, future_class_name,
                                                      future_class_parents,
                                                      new_attr)


class Foo(object, metaclass=UpperAttrMetaClass):
    bar = 'bip'


print(hasattr(Foo, 'bar'))
print(hasattr(Foo, 'BAR'))

f = Foo()
print(f.BAR)
