
"""
题目：求1+2!+3!+...+20!的和。

程序分析：此程序只是把累加变成了累乘。
"""

def sumfactor (x):
    ret =0
    temp=1
    for i in range(1,x+1):
        temp*=i
        ret+=temp
    return ret


a=sumfactor(20)
print(a)
