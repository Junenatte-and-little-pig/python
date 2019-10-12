# -*- encoding: utf-8 -*-


# 单继承
class Person(object):
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def __str__(self):
        return "大家好，我是{0}，今年{1}岁。".format(self.__name, self.__age)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if 0 <= age <= 150:
            self.__age = age
        else:
            print("请输入正确的年龄")


class Student(Person):
    def __init__(self, name, age, school, classname):
        super(Student, self).__init__(name, age)
        self.__school = school
        self.__classname = classname

    @property
    def name(self):
        return super(Student, self).name

    @name.setter
    def name(self, name):
        super(Student, self).name = name

    @property
    def age(self):
        return super(Student, self).age

    @age.setter
    def age(self, age):
        super(Student, self).age = age

    @property
    def school(self):
        return self.__school

    @school.setter
    def school(self, school):
        self.__school = school

    @property
    def classname(self):
        return self.__classname

    @classname.setter
    def classname(self, classname):
        self.__classname = classname

    def __str__(self):
        return "大家好，我是{0}，今年{1}岁。在{2}上学，是{3}班的学生。".format(
            super(Student, self).name,
            super(Student, self).age,
            self.school,
            self.classname)


class Employee(Person):
    def __init__(self, name, age, workplace, status):
        super(Employee, self).__init__(name, age)
        self.__workplace = workplace
        self.__status = status

    @property
    def name(self):
        return super(Employee, self).name

    @name.setter
    def name(self, name):
        super(Employee, self).name = name

    @property
    def age(self):
        return super(Employee, self).age

    @age.setter
    def age(self, age):
        super(Employee, self).age = age

    @property
    def workplace(self):
        return self.__workplace

    @workplace.setter
    def workplace(self, workplace):
        self.__workplace = workplace

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status):
        self.__status = status

    def __str__(self):
        return "大家好，我是{0}，今年{1}岁。在{2}上班，职位是{3}。".format(
            super(Employee, self).name,
            super(Employee, self).age,
            self.workplace,
            self.status)


p1 = Person("张三", 18)
s1 = Student("张三", 18, "南师大", "软件工程")
e1 = Employee("张三", 30, "华为", "java工程师")
print(str(p1))
print(str(s1))
print(str(e1))
