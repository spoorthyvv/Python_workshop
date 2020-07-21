def test_prime(n):
    if (n==1):
        return False
    elif (n==2):
        return True;
    else:
        for x in range(2,n):
            if(n % x==0):
                return False
        return True
no=int(input("Enter the number"))
if (test_prime(no)) is True :
    print(" {0} is a prime no".format(no))
else:
     print(" {0} is not a prime no".format(no))
