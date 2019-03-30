
"""
题目：求输入数字的平方，如果平方运算后小于 50 则退出。

程序分析：无
"""

out=False
all=0
while True:
    temp=int(input("输入一个数字："))
    all+=temp**2
    print("平方=%d"%all)
    if temp**2<50:
        break
