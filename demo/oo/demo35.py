# -*- encoding: utf-8 -*-
def line_conf(a, b):
    def line(x): # 闭包 调用域内变量
        return a * x + b

    return line


line1 = line_conf(1, 1)
line2 = line_conf(4, 5)
print(line1(5)) # same as line_conf(1, 1)(5)
print(line2(5))
