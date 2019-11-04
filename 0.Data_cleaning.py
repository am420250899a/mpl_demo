# -.- coding:utf-8 -.-
"""
Created on 2019-11-02 20:55
@author: cuizc
"""
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

power = pd.read_csv('household_power_consumption_1000.txt', sep=";")

print(power.head())
print(power.info())
# 统计值，包括平均数，标准差，中位数，最小值，最大值，25%分位数，75%分位数。
print(power.describe())

power["Global_active_power"].plot()
plt.show()