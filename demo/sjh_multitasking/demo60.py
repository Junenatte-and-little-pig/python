# -*- encoding: utf-8 -*-
import multiprocessing
import os


def run_proc(name):
    print('Child process {0} {1} Running '.format(name, os.getpid()))


if __name__ == '__main__':
    print('Parent process {0} is Running'.format(os.getpid()))
    for i in range(5):
        p = multiprocessing.Process(target=run_proc, args=(str(i),))
        print('process start')
        p.start()  # 创建进程
        p.join()  # 同步进程
        print('Process close')
