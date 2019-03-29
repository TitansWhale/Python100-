
"""
题目：求100之内的素数。

程序分析：无。

"""

from math import sqrt

def isSuShu(x):
    for i in range(2,int(sqrt(x)+1)):
        if x %i==0:
            return False

    return True


def qiuSuShu(start,end):
    ret=[]
    for i in range(start,end):
        if(isSuShu(i)):
            ret.append(i)
    return ret


a=qiuSuShu(2,100)
print(a)