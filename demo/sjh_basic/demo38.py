# -*- encoding: utf-8 -*-

# 二进制数 0b
# 八进制数 0o
# 十六进制 0x

print(bin(18))  # 0b10010
print(oct(18))  # 0o22
print(hex(18))  # 0x12

print(int("0b10010", 2))
print(int("0o22", 8))  # same as print(int("022",8))
print(int("0x12", 16))

# ValueError: invalid literal for int() with base 8: '0b10010'
# print(int("0b10010",8))
