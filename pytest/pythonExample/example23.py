
"""
   *
  ***
 *****
*******
 *****
  ***
   *
"""

#输入层数
def prin(x):
    #控制列
    height = (x-1)*2+1
    midd=height//2
    
    for i in range(height):
        a=""
        for j in range(height):            #(x-1)*2+1  =  水平大小
            if i<=midd:
                if(abs(j-midd))<=i:
                    a+='*'
                else:
                    a+=' '
            else:
                 if abs(j-midd)<= height%i-1:
                    a+='*'
                 else:
                    a+=' '
        print(a)

prin(4)
        



