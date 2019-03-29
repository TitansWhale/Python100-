"""
题目：利用递归方法求5!。
"""

def fact(x):
    if x==1:
        return 1
    else :
        return x*(fact(x-1))

print(fact(5))
