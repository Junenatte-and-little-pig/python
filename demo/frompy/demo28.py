# -*- encoding: utf-8 -*-
import random

print(random.seed())
print(random.random())  # 0~1
print(random.uniform(10, 1))  # same as print(random.uniform(1,10)
print(random.randint(1, 10))  # [1, 10]
print(random.randrange(1, 10))  # [1,10)

print(random.triangular(0, 10, 3))  # 三角分布
print(random.gauss(5, 10))  # 高斯分布
print(random.betavariate(2, 5))  # beta β分布
print(random.expovariate(10))  # 指数分布
print(random.gammavariate(5, 10))  # 伽马分布
print(random.lognormvariate(5, 10))  # 对数正态分布
print(random.normalvariate(5, 10))  # 正态分布
print(random.vonmisesvariate(2, 5))  # 冯米塞斯分布
print(random.paretovariate(2))  # 帕累托分布
print(random.weibullvariate(2, 5))  # 韦伯分布

li = [random.randint(1, 100) for x in range(0, 10)]
print(li)
random.shuffle(li)  # return None
print(li)
print(random.choice(li))
print(random.choices(li, weights=[1,2,3,4,5,6,7,8,9,10], k=3))
# same as print(random.choices(li,cum_weights=[1,3,6,10,15,21,28,36,45,55],k=3))
# means li[0] has 1/55 probability to be selected, etc
print(random.sample(li, 3))
