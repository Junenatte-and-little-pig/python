# -*- encoding: utf-8 -*-
import pickle # 用于python特有的类型和python的数据类型间进行转换

pd = [1, 2, 3, 4, 5]
str = pickle.dumps(pd)
print(str)
print(pickle.loads(str))
with open("pickle.txt", "wb") as f:
    pickle.dump(pd, f)
with open("pickle.txt", "rb") as f:
    print(pickle.load(f))
