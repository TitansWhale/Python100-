"""
题目：模仿静态变量的用法。

程序分析：无。

"""

def varfunc():
    var=0
    print("var=%d"%var)
    var +=1

for i in range(3):
    varfunc()

class Static:
    staticVar=5
    def varFunc(self):
        self.staticVar+=1
        print(self.staticVar)

a = Static()
for i in range(3):
    a.varFunc()
    
