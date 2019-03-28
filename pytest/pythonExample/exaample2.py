
i = int(input("净利润:"))
arr=[100    ,60     ,40     ,20     ,10     ,0]
rat=[0.01   ,0.015  ,0.03   ,0.05   ,0.075  ,0.1]

r= 0
for idx in range(0,6):
    if i>arr[idx]:
        r+=(i-arr[idx])*rat[idx]
        print((i-arr[idx])*rat[idx])
        i=arr[idx]
print(r)