# -*- encoding: utf-8 -*-
import copy

a = [1, 2, 3, 4, 5]
b = a  # 浅拷贝 拷贝引用而不引用内容 指定别名 后续操作相互影响
print("b:%s" % b)
print(a == b)  # 内容的相等
print(a is b)  # 引用对象的相等

c = copy.deepcopy(a)  # 深拷贝 全部拷贝 在另外的地址空间存放相同的内容 后续操作无关
print("c:%s" % c)
print(a == c)
print(a is c)

d = copy.copy(a)  # 对不可变类型浅拷贝 对可变类型则变成深拷贝
print("d:%s" % d)
print(a == d)
print(a is d)

a.append(6)
print("a:%s" % a)
print("b:%s" % b)
print("c:%s" % c)
print("d:%s" % d)

a1 = (0, 9, 8, 7, 6)
b1 = a1  # 浅拷贝 拷贝引用而不引用内容 指定别名 后续操作相互影响
print("b1:" + "%s" * len(b1) % b1)
print(a1 == b1)
print(a1 is b1)

c1 = copy.deepcopy(a1)  # 深拷贝 全部拷贝 在另外的地址空间存放相同的内容 后续操作无关
print("c1:" + "%s" * len(c1) % c1)
print(a1 == c1)
print(a1 is c1)

d1 = copy.copy(a1)  # 对不可变类型浅拷贝 对可变类型则变成深拷贝
print("d1:" + "%s" * len(d1) % d1)
print(a1 == d1)
print(a1 is d1)
