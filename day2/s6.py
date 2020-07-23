d={0:'',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',\
   10:'ten',11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',\
   17:'seventeen',18:'eightteen',19:'nineteen',20:'twenty',30:'thirty',40:'fourty',50:'fifty',\
   60:'sixty',70:'seventy',80:'eighty',90:'ninty'}

num=int(input("Enter the integer between 1 to 99:"))
if (num<=20):
      print(d[num])
if(num>20 and num<100):
        if num%10==0:       
            print(d[num])
        else:
            print(d[num//10*10]+" "+d[num%10])
