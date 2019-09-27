# -*- encoding: utf-8 -*-


def show(self):
    print(self.school)


ObjectClass = type("ObjectClass", (object,), {"school": "大学", "show": show})
print(ObjectClass)
print(ObjectClass())
help(ObjectClass)
ObjectClass().show()
ObjectClass.name="南京师范"
print(hasattr(ObjectClass,"name"))
print(ObjectClass.name)
