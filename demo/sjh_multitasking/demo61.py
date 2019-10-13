# -*- encoding: utf-8 -*-
import multiprocessing
import os
import time


def run_task(name):
    print('Task {0} pid {1} is running, parent id is {2}'.format(name,
                                                                 os.getpid(),
                                                                 os.getppid()))
    time.sleep(1)
    print('Task {0} end.'.format(name))


if __name__ == '__main__':
    print('current process {0}'.format(os.getpid()))
    # 设定池内进程数
    p = multiprocessing.Pool(processes=3)
    for i in range(6):
        p.apply_async(run_task, args=(i,))  # 非阻塞
        # p.apply(run_task, args=(i,))  # 阻塞
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All processes done!')
