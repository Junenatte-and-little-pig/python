# -*- encoding: utf-8 -*-

import builtins

keywords = dir(builtins)
print(keywords)
classes = []
members = []
keyFunc = []
for k in keywords:
    if k.isalpha():
        if k.islower():
            keyFunc.append(k)
        else:
            classes.append(k)
    else:
        members.append(k)
print(classes)
# 内置类
'''
['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BlockingIOError', 'BrokenPipeError', 
'BufferError', 'BytesWarning', 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError', 'ConnectionRefusedError', 
'ConnectionResetError', 'DeprecationWarning', 'EOFError', 'Ellipsis', 'EnvironmentError', 'Exception', 'False', 
'FileExistsError', 'FileNotFoundError', 'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 
'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError', 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 
'LookupError', 'MemoryError', 'ModuleNotFoundError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented', 
'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError', 
'RecursionError', 'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning', 'StopAsyncIteration', 
'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 'TimeoutError', 'True', 
'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 
'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 'WindowsError', 'ZeroDivisionError']'''
print(members)
# 内置成员
'''
['__build_class__', '__debug__', '__doc__', '__import__', '__loader__', '__name__', '__package__', '__spec__']
'''
print(keyFunc)
# 内置函数
'''['abs', 'all', 'any', 'ascii', 'bin', 'bool', 'breakpoint', 'bytearray', 'bytes', 'callable', 'chr', 
'classmethod', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 
'exec', 'exit', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 
'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 
'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr', 
'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 
'vars', 'zip'] '''

# abs绝对值函数
print(abs(10))  # 10
print(abs(-10))  # 10
# all判断列表/元组中是否有空元素 全非空True 有空False
print(all([1, 2, 3]))  # True
print(all([0, 1]))  # False
print(all(('a', 'b', 'c')))  # True
print(all(('a', '', 'c')))  # False
print(all([]))  # True
print(all(()))  # True
# any判断列表/元组中是否全为空元素 全空True 有非空False
print(any([0, '', False]))  # True
print(any([0, 1]))  # False
print(any(('', False, 0)))
print(any(('a', '', 'c')))  # False
print(any([]))  # False
print(any(()))  # False
# ascii
# bin返回二进制
print(bin(12))  # 0b1100
# bool返回布尔类型
print(bool(1))  # True
print(bool(0))  # False
print(bool('a'))  # True
print(bool(''))  # False
print(bool())  # False
# breakpoint
# bytearray返回字节数组
print(bytearray())  # bytearray(b'')
print(bytearray(5))  # bytearray(b'\x00\x00\x00\x00\x00')
print(bytearray([1, 2, 3]))  # bytearray(b'\x01\x02\x03')
print(bytearray('bytearray', 'utf-8'))  # bytearray(b'bytearray')
# bytes
# callable判断是否可调用
print(callable(1))  # False
print(callable(callable))  # True
# chr返回ascii对应字符
print(chr(65))  # A
# compile返回字符串代码对象 single单行语句 exec模块 eval表达式计算
exec(compile('print("hehe")', '', 'single'))  # hehe
exec(compile('print("haha")', '', 'exec'))  # haha
print(eval(compile('3+4*5', '', 'eval')))  # 23
# complex返回复数
print(complex(1))  # 1+0j
print(complex(1, 2))  # 1+2j
print(complex("1"))  # 1+0j
print(complex("1+2j"))  # 1+2j
# copyright
# credits
# delattr
# dict
# dir
# divmod
# enumerate
# eval
# exec
# exit
# filter
# float
# format
# frozenset
# getattr
# globals
# hasattr
# hash
# help
# hex
# id
# input
# int
# isinstance
# issubclass
# iter
# len
# license
# list
# locals
# map
# max
# memoryview
# min
# next
# object
# oct
# open
# ord
# pow
# print
# property
# quit
# range
# repr
# reversed
# round
# set
# setattr
# slice
# sorted
# staticmethod
# str
# sum
# super
# tuple
# type
# vars
# zip

# classmethod修饰符 修饰对象不需要被实例化就能被调用 第一个参数为cls
