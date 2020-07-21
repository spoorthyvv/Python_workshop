loop = 1 # 1 means loop; anything else means don't loop.
choice = 0 # This variable holds the user's choice in the menu

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b

while loop == 1:
    # Print what options you have
    print("Welcome to calculator.py")
    print("your options are:")
    print(" ")
    print("1) Addition")
    print("2) Subtraction")
    print("3) Multiplication")
    print("4) Division")
    print("5) Quit calculator.py")
    print(" ")
   try:
        choice = int(input("Choose your option: "))
   except:
        print('please enter a valid number for option')
    print(" ")
    print(" ")
   if choice == 1:
        x = int(input(“Enter 1st no: "))
        y = int(input("Enter 2nd no: "))
        print("The answer is ",add(x,y))

   elif choice == 2:
        x = int(input("Enter 1st no: "))
        y = int(input("Enter 2nd no: "))
        print("answer is ",sub(x,y))
  
   elif choice == 3:
        x = int(input("Enter 1st no: "))
        y = int(input("Enter 2nd no: "))
        print("answer is ",mul(x,y))

   elif choice == 4:
        x = int(input("Enter 1st no: "))
        y = int(input("Enter 2nd no: "))
        print("answer is ",div(x,y))

   elif choice == 5:
        loop = 0
     
   else:
        print("please choice a valid option from 1 to 5")
        choice=0
	print ("Thank-you for using calculator.py!")




