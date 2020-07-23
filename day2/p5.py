import numpy as np
List=[]
num=int(input("Enter the number of elements"))
print('Enter the elements: ')
for i in range(num):
  List.append(int(input()))
print('Average Of The Numbers Is: ',np.mean(List))
