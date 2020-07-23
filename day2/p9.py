

List=[]
for i in range(0,5):
    usn=input('Enter RollNumber: ')
    name=input('Enter Student Name: ')
    List.append((name,usn))
 
print(sorted(List, key = lambda x: x[1]))


