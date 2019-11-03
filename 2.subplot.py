# -.- coding:utf-8 -.-
"""
Created on 2019-11-03 11:09
@author: cuizc
"""

import matplotlib.pyplot as plt
import numpy as np

"""
————————————————
版权声明：本文为CSDN博主「thginWalker」的原创文章，遵循CC4.0 BY - SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/XZ2585458279/article/details/89633445
"""

"""
plt.subplot(234) 其中2表示行数，3表示列数，4表示第4个图
"""


# 格子划分
def default_grid():
    x = np.arange(1, 100)

    plt.subplot(221)
    plt.plot(x, x)

    plt.subplot(222)
    plt.plot(x, -x)

    plt.subplot(223)
    plt.plot(x, x * x)

    plt.subplot(224)
    plt.plot(x, np.log(x))

    plt.show()


# 占用多行或者多列，可以留空
def mul_cr():
    x = np.arange(1, 100)

    # 多行
    plt.subplot(221)
    plt.plot(x, x)

    plt.subplot(223)
    plt.plot(x, -x)

    plt.subplot(122)
    plt.plot(x, x * 2)
    plt.show()

    # 多列
    plt.subplot(331)
    plt.plot(x, x)

    plt.subplot(332)
    plt.plot(x, -x)

    plt.subplot(313)
    plt.plot(x, x * 2)
    plt.show()


if __name__ == '__main__':
    # default_grid()
    mul_cr()
