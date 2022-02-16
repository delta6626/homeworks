# Program to calculate area and circumference of a circle.
def calc(radius):
    area = str(3.14*radius**2)+" units"
    circumference = str(2*3.14*radius)+ " units"
    print("Area: ",area," Circumference: ", circumference)

calc(5)
calc(10)