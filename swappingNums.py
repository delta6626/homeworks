# A program to swap 2 numbers without using a temporary variable
x = int(input("Enter X : "))
y = int(input("Enter Y : "))
x, y = y, x
print("Swapping complete.")
print("X:", x, " Y:", y)
