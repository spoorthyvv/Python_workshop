import math
List=[]
for x in range(500,1000):
    root=math.sqrt(x)
    if int(root+0.5)**2==x:
        if x%5==0:
            List.append(x)
print(List)
