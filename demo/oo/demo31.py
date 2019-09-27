# -*- encoding: utf-8 -*-
def upper_attr(future_class_name, future_class_parents, future_class_attr):
    new_attr = {}
    for name, value in future_class_attr.items():
        if not name.startswith("__"):
            new_attr[name.upper()] = value
    # 调用type来创建一个类
    return type(future_class_name, future_class_parents, new_attr)


class Foo(object, metaclass=upper_attr):
    bar = 'bip'


print(hasattr(Foo, 'bar'))
print(hasattr(Foo, 'BAR'))

f = Foo()
print(f.BAR)
