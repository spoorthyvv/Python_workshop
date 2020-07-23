# Keys and Values example
d={}
print (" The dictionary elements are")
for i in range(1,21):
    d[i]=i**2
print (d)
# To print key and values
print (" Key==> Value are")
for (k,v) in d.items():	
    print(k,"==>",v)
# To print key only
print ("\nTo print key only")
for k in d.keys():	
     print(k, end=" ")
#To print value only
print ("\nTo print values only")
for v in d.values():	
    print(v, end=" ")
