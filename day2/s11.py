file1 = '/content/first.txt'
file2 = '/content/second.txt'

with open(file1,'r') as f:
 with open(file2, "w") as f1:
  for line in f:
   f1.write(line)
