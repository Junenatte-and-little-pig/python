# -*- encoding: utf-8 -*-


class MyException(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


def show(name):
    if len(name) <= 3:
        raise MyException("not wanted name")
    print(name)


try:
    show("hahahahaha")
    show("ha")
except MyException as e:
    print(e)
