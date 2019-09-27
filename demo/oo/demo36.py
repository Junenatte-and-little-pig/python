# -*- encoding: utf-8 -*-
def de(added):
    def dec(func):
        def wrapped(value):
            print(added)
            return func(value + added)

        return wrapped

    return dec


@de("world")
def show(value):
    print("*" * 20)
    return value


print(show("hello"))  # same as de("world")(show)("hello")
