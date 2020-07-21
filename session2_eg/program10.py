while True:
     try:
         x = int(input("Please enter a number: "))
         print(" That was valid number. Thank you")
         break
     except ValueError:
         print("Oops!  That was no valid number.  Try again...")




