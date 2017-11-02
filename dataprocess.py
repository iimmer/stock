
"""
股票分析

@author: lzm
"""
import os
import numpy as np
import pandas as pd

# 设置数据所在目录
stockDataDir = "E:/StockDateBase"

# 列出目录内所有文件清单
allFilesList = np.array(os.listdir(stockDataDir))


#导入数据到h5文件
for indx in allFilesList:
    
    # 要打开的文件路径
    fullPath = stockDataDir + "/" + indx
   
    nameList = ["Date", "Open", "Hight", "Low", "Close", "Volume", "Total"]
    #导入的DataFrame
    a = pd.read_csv(fullPath,
                    encoding="gb2312",
                    header=None,
                    names=nameList)


    # 去除包含Nan的行
    a.dropna(inplace=True)

    # 将Date项由字符串转为日期格式
    a.Date = pd.to_datetime(a.Date)

    #在本目录下创建(打开)一个h5文件
    h5 = pd.HDFStore('database.h5', 'a')

    h5[indx[:-4]]=a

h5.close()





