file = '/content/first.txt'
with open (file,'r') as f:
 for line in f:
  l=line.split()
  l.reverse() 
  st= " ".join(l)
  print (st)
