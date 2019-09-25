# -*- encoding: utf-8 -*-


# 多继承
class A(object):
    def show(self):
        print("A".center(10, "-"))


class B(object):
    def show(self):
        print("B".center(10, "-"))


class C(B, A):
    def show(self):
        print("C".center(10, "-"))


# 多态 鸭子模型
def print_show(obj):
    obj.show()


c = C()
print(C.__mro__)
c.show()
print_show(c)