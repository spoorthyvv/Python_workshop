#Python Program to count the number of lines in a text file. 
file='/content/first.txt'
num_words = 0
with open(file, 'r') as f:
 for line in f:
   words = line.split()
   print(words)
   num_words += len(words)
   print("Number of words:")
   print(num_words)
