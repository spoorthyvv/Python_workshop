''' Python3 program to calculate Volume and  
    Surface area of Cone'''
  
# assigning value Of PI 
pi =3.142
  
# Function to calculate Volume of Cone 
def volume(r, h): 
    return (1 / 3) * pi * r * r * h 
  
# Function To Calculate Surface Area of Cone 
def surfacearea(r, s): 
    return pi * r * s + pi * r * r 
  
# Driver Code 
radius = float(input("Enter the radius")) 
height = float(input("Enter the height")) 
slat_height = float(input("Enter the slant height")) 
print( "Volume Of Cone : ", volume(radius, height) ) 
print( "Surface Area Of Cone : ", surfacearea(radius, slat_height) )
