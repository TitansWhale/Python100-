"""
题目：一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数。

程序分析：请参照程序Python 练习实例14。
"""
import numpy as np
from math import sqrt
#d打印start到end 的素数 1-100
def outSuShu(start,end):
	ret=[]
	for m in range(start,end+1):
		leap=1
		k = int(sqrt(m + 1))
		for i in range(2,k + 1):
			if m % i == 0:
				leap = 0
				break
		if leap == 1:
			ret.append(int(m))    
	return ret        

#计算因数
def yinshu(x):
    ret=[]
    for i in range(1,x//2+1):
        if x%i==0:
            ret.append(int (i))
    return ret

#计算完数
def wanshu(end):
    ret=[]
    temp=yinshu(end)
    for i in range(1,end+1):
        temp = yinshu(i)
        if i ==sum(temp):
            ret.append(i)
    return ret

out=wanshu(1000)
print(out)