"""
题目：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。

程序分析：关键是计算出每一项的值。
"""

def outA(x,y):
    i=0
    ret=0
    temp10=1
    while i<y:
        ret+=temp10*x
        temp10*=10
        i+=1
    return ret

n=4
a=4
sum=0
for i in range(1,n+1):
    temp=outA(a,i)
    sum+=temp
    
    print(temp)

print(sum)