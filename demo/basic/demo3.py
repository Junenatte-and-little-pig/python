# -*- encoding: utf-8 -*-

i = 1
sum = 0
while i < 10:
    sum += i
    i += 1
print(sum)

i = 1
j = 1
for i in range(1, 10):
    for j in range(i, 10):
        print("%2d *%2d = %2d" % (i, j, i * j), end="\t")
    print()

i = 1
j = 1
for i in range(1, 10):
    for j in range(1, i + 1):
        print("%2d *%2d = %2d" % (i, j, i * j), end="\t")
    print()
