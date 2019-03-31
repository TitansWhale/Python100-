"""
题目 取一个整数a从右端开始的4〜7位。

程序分析 可以这样考虑：


"""
a=eval(input())

b=0b1111
a=a>>3
print(bin(a&b))
