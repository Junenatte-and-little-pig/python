# -*- encoding: utf-8 -*-

with open('test.txt', 'w', encoding='utf-8') as f:
    f.write("这是一个测试文件\r")
    lines = ["这是测试文件的第一行\r", "这是测试文件的第二行\r", "这是测试文件的第三行\r"]
    f.writelines(lines)

with open('test.txt', 'r', encoding='utf-8') as f:
    for line in f:
        print(line, end="")
print()

with open('test.txt', encoding='utf-8') as origin, open('backup.txt', 'w', encoding='utf-8') as dest:
    for line in origin:
        dest.write(line)
