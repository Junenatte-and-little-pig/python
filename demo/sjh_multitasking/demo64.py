# -*- encoding: utf-8 -*-
from threading import Thread


def sayhi(name):
    print('%s say hello' % name)


if __name__ == '__main__':
    t = Thread(target=sayhi, args=('hh',))
    t.start()
    print('主线程')