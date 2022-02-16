# Program to calculate distance between 2 points
import math

x1 = float(input("Enter X1 : "))
y1 = float(input("Enter Y1 : "))
x2 = float(input("Enter X2 : "))
y2 = float(input("Enter Y2 : "))

# formula -> distance = sqrt((x2-x1)^2+(y2-y1)^2)

distance = math.sqrt((x2-x1)**2+(y2-y1)**2)
print(distance)