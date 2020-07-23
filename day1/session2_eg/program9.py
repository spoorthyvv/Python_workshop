flag = True

def div(a, b):  
       try:
            print("Finally the division of %d/%d is %f" % (a, b,a/b))
            global flag
            flag=False
       except ZeroDivisionError:
            print("Zero Division Error detected")
       else:
            print("Division is successful") 
       finally:
            if flag is True:
               print("Try again")     
            else:
               print("Thank you")
       
#global flag

while flag is True:
    div(int(input("Enter numerator")),int(input("Enter denominator")))

