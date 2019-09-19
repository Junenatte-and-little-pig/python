# -*- encoding: utf-8 -*-

nameSet = set()
print(type(nameSet))
nameSet = {"张三", "李四", "王五", "赵六", "孙七", "钱八", "周九"}
print(type(nameSet))
nameSet = {"张三", "李四", "王五", "赵六", "赵六", "孙七", "钱八", "周九"}
print(nameSet)
nameSet.add("张三")
print(nameSet)
nameSet.add("吴十")
print(nameSet)
nameSet.remove("孙七")  # 不存在会抛出KeyError
print(nameSet)
nameSet.discard("李四")  # 不会抛出KeyError
print(nameSet)
nameSet2 = {"张三", "李四", "王五", "赵六", "孙七", "钱八", "周九"}
print(nameSet2)
print(nameSet.difference(nameSet2))  # in nameSet and not in nameSet2
print(nameSet2.difference(nameSet))  # in nameSet2 and not in nameSet
print(nameSet.symmetric_difference(nameSet2))  # (in nameSet and not in nameSet2) or (in nameSet2 and not in nameSet)
print(nameSet.intersection(nameSet2))
print(nameSet.union(nameSet2))
print(nameSet.issubset(nameSet2))
print(nameSet.issuperset(nameSet2))
print(nameSet.isdisjoint(nameSet2))  # nameSet.intersection(nameSet2) == set()
print(nameSet.pop())
print(nameSet)
