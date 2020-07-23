# Python Program to count the number of lines in a text file. 
from google.colab import drive
drive.mount('/content/gdrive')
#Python Program to count the number of lines in a text file. 
file='/content/first.txt'
num_lines = 0
with open(file, 'r') as f:
 for line in f:
   num_lines += 1
   print("Number of lines:")
   print(num_lines)
