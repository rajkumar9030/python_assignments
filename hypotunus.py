import math
base = int(input("Enter base length of triangle: "))
height = int(input("Enter height length of triangle: "))
hypotenuse = math.sqrt(math.pow(base, 2) + math.pow(height, 2))
print("The length of the hypotenuse is:", hypotenuse)