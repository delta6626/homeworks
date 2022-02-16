# a quadratic equation solver
# x = (-b+/-(sqrt(b^2-4ac))/2a
import math
a = int(input("X^2 term :"))
b = int(input("X term : "))
c = int(input("Constant term : "))
result1 = (-b+math.sqrt((b**2)-4*a*c))/2*a
result2 = (-b-math.sqrt((b**2)-4*a*c))/2*a
print(result1,result2)
