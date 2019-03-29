
"""
题目：给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。

程序分析：学会分解出每一位数。
"""
#他是几位数int,逆序字符串
def out(a):
    count = 0
    outstr=""
    while a!=0:
        count+=1
        temp=a%10

        outstr+=str(temp)
        a//=10
    return count,outstr

print(out(123))