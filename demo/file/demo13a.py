# -*- encoding: utf-8 -*-

# 按块读取 适用于二进制文件
blockSize = 1024
with open('demo11.py', 'rb') as f:
    f.read(blockSize)
    for line in f:
        print("当前文件位置" + str(f.tell()))
        print(line)
