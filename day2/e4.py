x=0
l=[int(input(x)) for _ in range(int(input("Enter n")))]
print('even list is',[ i for i in l if i%2])
print('odd list is',[i for i in l if not i%2])
