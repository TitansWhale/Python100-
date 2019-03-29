
"""
题目：利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。

程序分析：无。
"""

def reverOutput(a,i):
    if i ==0:
        return
    print(a[i-1])
    reverOutput(a,i-1)

a="123456"
reverOutput(a,6)