n=int(input("Enter no of records"))
d={}
for i in range(1,n+1):
    name= input("Enter name %d"%(i))
    mark=int(input("Enter mark %d"%(i)))
    d[name]=mark
    print (d)
