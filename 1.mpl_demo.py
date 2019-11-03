# -.- coding:utf-8 -.-
"""
Created on 2019-11-02 20:56
@author: cuizc
"""
import numpy as np
import matplotlib.pyplot as plt
import random

"""
————————————————
版权声明：本文为CSDN博主「thginWalker」的原创文章，遵循CC4.0 BY - SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/XZ2585458279/article/details/89633445
"""

"""
python v3.7
matplotlib  v3.1.1
1.散点图：主要表现数据量因变量随自变量而变化，主要有正相关、负相关和不相关，样本量大，没有时序性。
2.折线图：主要表现某事物随时间的变化而变化，当然并不定非要是时间，样本有时序性。
3.条形图：主要以长方形的长度为变量的统计图表，常用来比较多个项目分类的数据大小。在这里我们主要分为默认条形图、横放条形图和层叠条形图。
4.直方图：由一系列高度不等的纵向条形组成，表示数据分布的情况。注意:直方图和条形图的区别在于直方图可连续，条形图不可连续。
5.饼状图：显示一个数据系列中各项的大小与各项总和的比例，其中饼状图中的数据显示为整个饼状图的百分比。
"""

"""
颜色表示
1. 8中颜色缩写
    缩写	全拼	颜色
    b	    blue	蓝色
    g	    green	绿色
    r	    red	    红色
    m	    magenta	品红色
    c	    cyan	青色
    y	    yellow	黄色
    k	    black	黑色
    w	    white	白色
2. 灰度表示：0 - 1，由深到浅
3. 16进制表示：R G B三种颜色每种颜色分成256个等级，写成两位16进制数，格式为 #RRGGBB，如#FF0000 表示红色
4. 元组表示：RGB三种颜色的0 - 1 的浮点值表示颜色深浅，如(0.1, 0.2, 0.3)
"""

"""
线条样式
符号	解释
-	    实线样式
–	    短横线样式
-.	    点划线样式
:	    虚线样式
"""

"""
点样式
符号	解释
,	    像素标记
o	    圆标记
v	    倒三角标记
^	    正三角标记
<	    左三角标记
>	    右三角标记
1	    下箭头标记
2	    上箭头标记
3	    左箭头标记
4	    右箭头标记
s	    正方形标记
p	    五边形标记
*	    星形标记
h	    六边形标记1
H	    六边形标记2
+	    加号标记
x	    X 标记
D	    菱形标记
d	    窄菱形标记
|	    竖直线标记
_	    水平线标记
"""


# 1.散点图
def scatter_demo():
    # 正相关
    N = 1000
    x = np.random.randn(N)
    y = x + np.random.randn(N) * 0.5
    plt.scatter(x, y)
    plt.show()

    # 负相关
    N = 1000
    x = np.random.randn(N)
    y = - x + np.random.randn(N) * 0.5
    plt.scatter(x, y)
    plt.show()

    # 不相关
    N = 1000
    x = np.random.randn(N)
    y = []
    for i in range(0, 1000):
        y.append(random.uniform(1, 1000))
    plt.scatter(x, y)
    plt.show()


# 2.折线图
def plot_demo():
    x = np.linspace(-10, 10, 5)
    y = x ** 2
    plt.plot(x, y)
    plt.show()


# 3.条形图
def bar_demo():
    N = 5

    y = [20, 10, 30, 25, 15]
    index = np.arange(N)

    # 默认条形图
    pl = plt.bar(x=index, height=y, width=0.8, bottom=5, align='center')
    plt.show()

    # 横放条形图
    pl = plt.barh(y=index, left=0, width=y, color='red', height=0.5)
    plt.show()

    # 上下层叠图
    index = np.arange(4)
    sales_BJ = [52, 55, 63, 53]
    sales_SH = [44, 66, 55, 41]
    bar_width = 0.3

    plt.bar(index, sales_BJ, bar_width, color='b')
    plt.bar(index, sales_SH, bar_width, color='r', bottom=sales_BJ)
    plt.show()

    # 左右层叠图
    plt.bar(index, sales_BJ, bar_width, color='b')
    plt.bar(index + bar_width, sales_SH, bar_width, color='r')
    plt.show()


# 直方图
def hist():
    mu = 100
    signa = 20
    x = mu + signa * np.random.randn(20000)  # 2000个数据

    plt.hist(x, bins=10, color='green', normed=True, edgecolor='k')
    plt.show()

    # 双向直方图
    x = np.random.randn(1000) + 2
    y = np.random.randn(1000) + 3
    plt.hist2d(x, y, bins=40)
    plt.show()


# 饼状图
def pie():
    labels = 'A', 'B', 'C', 'D'
    fracs = [15, 30, 45, 10]

    plt.axes(aspect=1)  # 将x与y轴比例变成1比1
    explode = [0, 0.2, 0, 0]  # 突出显示，远离中心
    # %f为格式化字符,参考https://www.cnblogs.com/crawer-1/p/8241882.html
    plt.pie(x=fracs, labels=labels, autopct='%0.1f%%', explode=explode, shadow=True)
    plt.show()


# 颜色
def color():
    y = np.arange(1, 5)
    plt.plot(y, color='r')  # 缩写
    plt.plot(y + 1, color='0')  # 灰度
    plt.plot(y + 2, color='#FF0000')  # 16进制
    plt.plot(y + 3, color=(1, 0, 0))  # 元组
    plt.show()


# 线条
def line_style():
    y = np.arange(1, 5)
    plt.plot(y, ls='-')  # 实线样式
    plt.plot(y + 1, ls='--')  # 短横线样式
    plt.plot(y + 2, ls='-.')  # 点划线样式
    plt.plot(y + 3, ls=':')  # 虚线样式
    plt.show()


# 点样式
def point_style():
    y = np.arange(5)
    plt.plot(y)
    plt.plot(y + 1, marker='o')  # marker属性会在画线的基础上画出点
    plt.plot(y + 2, 'o')
    plt.show()


if __name__ == '__main__':
    # scatter_demo()
    # plot_demo()
    # bar_demo()
    # hist()
    # pie()
    # color()
    # line_style()
    point_style()
