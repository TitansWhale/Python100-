
"""
题目：一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。

程序分析：无。
"""



a=123321

def isHuiwen(a):
    temp=str(a)
    tempT=temp
    temp=list(reversed(temp))
    temp="".join(temp);

    
    if temp==tempT:
        return True
    else :
        return False

print(isHuiwen(a))