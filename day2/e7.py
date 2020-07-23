#Python Program to sort the list according to the second element in the sublist.
a=[['A',34],['B',21],['C',26],['E',29]]
for i in range(0,len(a)):
    for j in range(i+1,len(a)):
        if(a[i][1]>a[j][1]):
            temp=a[j]
            a[j]=a[i]
            a[i]=temp
print(a)
