"""
题目：一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数。

程序分析：请参照程序Python 练习实例14。
"""

a=(2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97)

import numpy as np
#返回他所有的因数
def output(x):
    temp=[]
    while True:
        for da in a:
            if da==x:
                temp.append(da)
                return temp
            elif x % da == 0:
                temp.append(da)
                x/=da
                break;


for x in range(1,1001):
    temp=output(x)
    if x==sum(temp):
        print(x)
        print(temp)
