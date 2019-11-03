# -.- coding:utf-8 -.-
"""
Created on 2019-11-03 11:22
@author: cuizc
"""
import matplotlib.pyplot as plt
import numpy as np
import datetime
import matplotlib as mpl

"""
包括网格、图例、坐标轴的范围、坐标轴的刻度、添加坐标轴、注释、文字和Tex数学公式。
"""


# 加网格
def grid():
    x = np.arange(1, 10, 1)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    plt.plot(x, x * 2)
    # plt.grid(color='r')
    ax.grid(color='g')  # grid 方法，color指定网格颜色
    plt.show()


# 加图例
def legend():
    x = np.arange(1, 11, 1)

    plt.plot(x, x * 2, label="Noramal")
    plt.plot(x, x * 3, label="Fast")
    plt.plot(x, x * 4, label="Faster")
    plt.legend(loc=0)  # 添加图例(有很多参数) loc为0(自动选择放置位置),1,2,3,4,5,6,7,8,9,10
    # plt.legend(['Normal', 'Fast', 'New'])   # 指定图例, 按画图的顺序，依次对应，可以少，多了不显示
    plt.show()

    # # 面向对象方法
    # fig = plt.figure()
    # ax = fig.add_subplot(111)
    # l, = plt.plot(x, x, label='Inline label')
    # ax.legend()
    # fig.show()


# 坐标轴
def axis():
    x = np.arange(-10, 11, 1)
    plt.plot(x, x * x)
    # plt.axis([-5, 5, 20, 60])  # x轴的范围和y轴的范围
    # plt.xlim([-5, 5])  # 只管x轴不管y轴
    # plt.ylim([-5, 5])  # 只管y轴不管x轴
    # plt.xlim(xmin=-5, xmax=5)
    # plt.xlim(xmin=-5)  # 只调整一边
    plt.show()


# 刻度
def scale():
    x = np.arange(1, 11, 1)

    # ax = plt.plot(x, x)
    ax = plt.gca()  # 获取当前坐标轴
    # ax.locator_params(nbins=20)#nbins指坐标轴有多少格(x,y轴)
    ax.locator_params('x', nbins=20)  # nbins指坐标轴有多少格
    # ax.locator_params('y'nbins=20)#nbins指坐标轴有多少格
    # plt.show()

    # plt调整方法
    # plt.locator_params一样

    # 日期的调整

    fig = plt.figure()

    start = datetime.datetime(2015, 1, 1)
    stop = datetime.datetime(2016, 1, 1)
    delta = datetime.timedelta(days=1)

    dates = mpl.dates.drange(start, stop, delta)

    y = np.random.rand(len(dates))

    ax = plt.gca()

    ax.plot_date(dates, y, linestyle='-', marker='')
    date_format = mpl.dates.DateFormatter('%Y-%m-%d')  # 中文日期
    ax.xaxis.set_major_formatter(date_format)  # 进行设置
    fig.autofmt_xdate()  # 自适应日期
    plt.show()


# 添加轴
def add_axis():
    x = np.arange(2, 20, 1)

    y1 = x * x
    y2 = np.log(x)
    # plot方式
    # plt.plot(x,y1)
    # plt.twinx()#添加坐标轴
    # plt.plot(x,y2,'r')
    # plt.show()

    # 面向对象方式
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax1.plot(x, y1)
    ax1.set_ylabel('Y1')
    ax2 = ax1.twinx()  # 当然也可twiny
    ax2.plot(x, y2, 'r')
    ax2.set_xlabel('Compare Y1 and Y2')
    plt.show()


# 注释
def annotate():
    x = np.arange(-10, 11, 1)
    y = x * x
    plt.plot(x, y)
    plt.annotate("this is the bottom",
                 xy=(0, 5),  # 箭头坐标
                 xytext=(0, 20),  # 这行字的起始坐标  注:arrowprops(新版本不在支持)
                 arrowprops=dict(facecolor='r', frac=1, headwidth=10)  # frac是箭头占比
                 )
    plt.show()


# 添加文字
def add_text():
    x = np.arange(-10, 11, 1)
    y = x * x
    plt.plot(x, y)
    plt.text(-2, 40, 'function:y=x*x', family='serit', size=20, color='r', style='italic', weight=0)
    plt.text(-2, 20, 'function:y=x*x', family='fantasy', size=20, color='g', style='oblique', weight=1000,
             bbox=dict(facecolor='r', alpha=0.2))
    plt.show()


if __name__ == '__main__':
    # grid()
    # legend()
    # axis()
    # scale()
    # add_axis()
    # annotate()
    add_text()
