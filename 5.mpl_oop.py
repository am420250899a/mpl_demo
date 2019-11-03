# -.- coding:utf-8 -.-
"""
Created on 2019-11-03 11:01
@author: cuizc
"""
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 10, 1)
y = np.random.randn(len(x))

fig = plt.figure()

ax = fig.add_subplot(111)
l, = plt.plot(x, y)  # 注字母l并没有用
t = ax.set_title('object oriented')
plt.show()
