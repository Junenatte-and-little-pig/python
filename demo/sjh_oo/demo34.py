# -*- encoding: utf-8 -*-


def fib():
    a, b = 0, 1
    count = 1
    while count < 10:
        temp = yield b
        print(temp)
        count += 1
        s = a + b
        a = b
        b = s


f = fib()
for i in f:
    print(i)
    if i > 20:
        f.send("haha")
