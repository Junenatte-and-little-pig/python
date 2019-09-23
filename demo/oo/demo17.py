# -*- encoding: utf-8 -*-


# 单继承
class Person(object):
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def __str__(self):
        return "大家好，我是{0}，今年{1}岁。".format(self.__name, self.__age)

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age


class Student(Person):
    def __init__(self, name, age, school, classname):
        super(Student, self).__init__(name, age)
        self.__school = school
        self.__classname = classname

    def get_name(self):
        return super(Student, self).get_name()

    def set_name(self, name):
        super(Student, self).set_name(name)

    def get_age(self):
        return super(Student, self).get_age()

    def set_age(self, age):
        super(Student, self).set_age(age)

    def get_school(self):
        return self.__school

    def set_school(self, school):
        self.__school = school

    def get_classname(self):
        return self.__classname

    def set_classname(self, classname):
        self.__classname = classname

    def __str__(self):
        return "大家好，我是{0}，今年{1}岁。在{2}上学，是{3}班的学生。".format(
            super(Student, self).get_name(),
            super(Student, self).get_age(),
            self.__school,
            self.__classname)


class Employee(Person):
    def __init__(self, name, age, workplace, status):
        super(Employee, self).__init__(name, age)
        self.__workplace = workplace
        self.__status = status

    def get_name(self):
        return super(Employee, self).get_name()

    def set_name(self, name):
        super(Employee, self).set_name(name)

    def get_age(self):
        return super(Employee, self).get_age()

    def set_age(self, age):
        super(Employee, self).set_age(age)

    def get_workplace(self):
        return self.__workplace

    def set_workplace(self, workplace):
        self.__workplace = workplace

    def get_status(self):
        return self.__status

    def set_status(self, status):
        self.__status = status

    def __str__(self):
        return "大家好，我是{0}，今年{1}岁。在{2}上班，职位是{3}。".format(
            super(Employee, self).get_name(),
            super(Employee, self).get_age(),
            self.__workplace,
            self.__status)


p1 = Person("张三", 18)
s1 = Student("张三", 18, "南师大", "软件工程")
e1 = Employee("张三", 30, "华为", "java工程师")
print(str(p1))
print(str(s1))
print(str(e1))
