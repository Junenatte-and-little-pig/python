# -*- encoding: utf-8 -*-

import os
# os.rename("test.txt","rename.txt")
# os.remove("rename.txt")
# os.mkdir("test")
# os.rmdir("test")
print(os.getcwd())
os.chdir("D:/")
print(os.getcwd())
os.chdir("E:/Github/python/demo")
print(os.listdir("./"))

print(os.environ)
