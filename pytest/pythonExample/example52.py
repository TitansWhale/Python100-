"""
题目 学习使用按位或 | 。

程序分析 0|0=0; 0|1=1; 1|0=1; 1|1=1
"""

a=0o77
print(hex(a|3))
print(hex(a|3|7))