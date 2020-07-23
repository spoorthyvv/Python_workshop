#Instead of  forementioned 13 lines program, the equivalent 5 lines !
# Pythonic program is here ....

x=0
l=[int(input(x)) for _ in range(int(input("Enter how many elements")))]
m=[int(input(x)) for _ in range(int(input("Enter how many elements ")))]
new=l+m
new.sort()
print("Sorted list is:",new)
