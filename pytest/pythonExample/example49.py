
"""
题目：使用lambda来创建匿名函数。

程序分析：无
"""

MAX=lambda x,y:(x>y)*x+(x<y)*y
MIN=lambda x,y:(x>y)*y+(x<y)*x



a=1
b=2

print("max:%d"%MAX(a,b))
print("min:%d"%MIN(a,b))

