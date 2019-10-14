# -*- encoding: utf-8 -*-
import matplotlib.pyplot as plt

x_args = [x for x in range(0, 6)]
a_args = [x ** 2 for x in x_args]
b_args = [x ** 0.5 for x in x_args]
x_min = 0
x_max = 5
y_min = 0
y_max = 25
axis_range = [x_min, x_max, y_min, y_max]
# plt.plot(x_args, a_args)
# plt.plot(x_args, a_args, 'go')  # 指定样式的缩写形式
# plt.plot(x_args, a_args, color='green', marker='o', linestyle='dashed', linewidth=2, markersize=12)
# a_marker = {'color': 'green', 'marker': '3', 'linestyle': 'dashed', 'linewidth': '2', 'markersize': '12'}
# plt.plot(x_args, a_args, **a_marker)
plt.plot(x_args, a_args, 'r3', x_args, b_args, 'bp')
plt.axis(axis_range)  # 指定轴范围
plt.show()
