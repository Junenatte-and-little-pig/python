# -*- encoding: utf-8 -*-


try:
    # open("asd.txt", "r")
    print(1 / 0)
except (IOError, ZeroDivisionError) as e:  # 仅代表对多异常采取相同的行为
    print(e)
else:
    print("no exception")
finally: # 有无异常都会被执行
    print("hello")
