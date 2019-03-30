
"""
题目：求一个3*3矩阵主对角线元素之和。

程序分析：利用双重for循环控制输入二维数组，再将a[i][i]累加后输出。

"""
a=[[0]*3]*3

for i in range(3):
    for j in range(3):
        a[i][j]=i+j

all=0;
for i in range(3):
    for j in range(3):
        if i==j:

            all+=a[i][j]

print(all)