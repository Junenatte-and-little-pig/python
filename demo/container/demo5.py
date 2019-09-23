# -*- encoding: utf-8 -*-

namelist = ["张三", "李四", "王五", "赵六", "孙七", "钱八", "周九"]
print(namelist)

for n in namelist:
    print(n, end=" ")
print()
index = 0
while index < len(namelist):
    print(namelist[index], end=" ")
    index += 1
print()
for i in range(0, len(namelist)):
    print(namelist[i], end=" ")
print()
for i in range(len(namelist) - 1, -1, -1):
    print(namelist[i], end=" ")
print()
for n in namelist[::-1]:
    print(n, end=" ")
print()

namelist.append("吴十")
print(namelist)
namelist.extend(["郑十一", "王十二"])
print(namelist)
namelist.insert(5, 1)
print(namelist)

namelist.pop()  # 返回元素值
print(namelist)
namelist.pop(5)  # 返回元素值
print(namelist)
namelist.remove("孙七")
print(namelist)
cp = namelist.copy()
print(cp)
cp.clear()
print(cp)

namelist.reverse()
print(namelist)
namelist.sort()
print(namelist)
namelist.sort(reverse=True)
print(namelist)
