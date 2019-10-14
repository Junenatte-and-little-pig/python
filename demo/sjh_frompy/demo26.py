# -*- encoding: utf-8 -*-
import random
import time

print(time.time())
print(time.localtime())  # same as print(time.localtime(time.time()))
# tm_year=2019, tm_mon=9, tm_mday=26, tm_hour=0, tm_min=4, tm_sec=17, tm_wday=3, tm_yday=269, tm_isdst=0
print(time.gmtime())  # same as print(time.gmtime(time.time()))
ti = (2019, 9, 26, 0, 4, 17, 3, 269, 0)
print(time.mktime(ti))
print(time.asctime(ti))
print(time.ctime())  # same as print(time.ctime(time.time()))

# count sleep time
pc1 = time.perf_counter()
r1 = [random.random() for x in range(0, 100000)]
time.sleep(1)
pc2 = time.perf_counter()
print(pc2 - pc1)

# ignore sleep time
pt1 = time.process_time()
r2 = [random.random() for y in range(0, 100000)]
time.sleep(1)
pt2 = time.process_time()
print(pt2 - pt1)
# and more precise, there are time_ns(), perf_counter_ns(), process_time_ns()
# and they return with an int
print(time.time_ns())

'''
%y 两位数的年份表示（00-99）
%Y 四位数的年份表示（000-9999）
%m 月份（01-12）
%d 月内中的一天（0-31）
%H 24小时制小时数（0-23）
%I 12小时制小时数（01-12） 
%M 分钟数（00=59）
%S 秒（00-59）
%a 本地简化星期名称
%A 本地完整星期名称
%b 本地简化的月份名称
%B 本地完整的月份名称
%c 本地相应的日期表示和时间表示
%j 年内的一天（001-366）
%p 本地A.M.或P.M.的等价符
%U 一年中的星期数（00-53）星期天为星期的开始
%w 星期（0-6），星期天为星期的开始
%W 一年中的星期数（00-53）星期一为星期的开始
%x 本地相应的日期表示
%X 本地相应的时间表示
%Z 当前时区的名称
%% %号本身 
'''
print(time.strftime("%Y-%m-%d %H:%M:%S", ti))
print(time.strptime("2019-09-26 00:04:17", "%Y-%m-%d %H:%M:%S"))
