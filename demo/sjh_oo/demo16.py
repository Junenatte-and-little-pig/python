# -*- encoding: utf-8 -*-

# 类只能重写 没有重载 故只有一个构造函数
class Student(object):
    # 此为类的对象 可以直接被类名调用 不推荐
    # name = None

    def __init__(self, name, age, birthday, classname):
        """
        :param name: str
        :param age: int
        :param birthday: str with format 'yyyy-MM-dd'
        :param classname: str
        """
        print("对象构造...")
        # 属性前加__保护对象的属性 防止直接访问
        self.__name = name
        self.__age = age
        self.__birthday = birthday
        self.__classname = classname

    def __str__(self):
        return "我是{0} 我今年{1}岁了，我的生日是{2}，我是{3}班的学生".format(self.__name,
                                                          self.__age,
                                                          self.__birthday,
                                                          self.__classname)

    def __del__(self):
        print("对象释放...")

    # 通过get/set方法对对象的属性进行查看和修改 推荐 更加的安全 可以对数据进行控制
    # @property方法调用时无括号
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

    @property
    def birthday(self):
        return self.__birthday

    @birthday.setter
    def birthday(self, birthday):
        self.__birthday = birthday

    @property
    def classname(self):
        return self.__classname

    @classname.setter
    def classname(self, classname):
        self.__classname = classname

    @staticmethod
    def hello():
        print("你好")

    @classmethod
    def hello_stu(cls):
        print("你好")


s1 = Student("张三", 18, "2000-01-01", "1602")
print(str(s1))
s1.age = 20
print(s1.age)
print(str(s1))
Student.hello()
Student.hello_stu()
