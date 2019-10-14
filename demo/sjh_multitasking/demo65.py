# -*- encoding: utf-8 -*-
import time
from threading import Thread


class Sayhi(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        time.sleep(2)
        print('%s say hello' % self.name)


if __name__ == '__main__':
    t = Sayhi('hh')
    t.start()
    print('主线程')
