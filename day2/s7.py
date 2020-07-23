d = {"Pierre": 42, "Anne": 33, "Zoe": 24}
#Use the sorted function and operator module
import operator
sorted_d = sorted(d.items(), key=operator.itemgetter(1))
print(sorted_d)
sorted_a= sorted(d.items(), key=operator.itemgetter(1),reverse=True)
print(sorted_a)
