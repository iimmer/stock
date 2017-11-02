# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 11:33:43 2017
未来几天内的最大值,最小值.
@author: zhemin.liu
"""

import pandas as pd

# 打开数据库
h5 = pd.HDFStore('allstockdata.h5', 'r')

# 读入股票数据603020
stock = h5['SH603020']

# 在stock中新增加一列用于储层未来5天收盘价的最大值

nday = 5  # 未来天数 5 shift(-5)是上移5天
stock['maxIn5'] = stock.Close.rolling(nday).max().shift(-1 * nday)
stock['pct'] = (stock.maxIn5 - stock.Close) / stock.Close * 100

