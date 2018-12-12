import math

print("I will find the hypotenuse of a triangle if you give the lengths of its two sides.")

o = 1
a = 1


o = int(input("What length in centimeters is one side?"))

a = int(input("What length in centimeters is the other side?"))

osq = int(o * o)
asq = int(a * a)

x = int(osq + asq)

h = math.sqrt(x)
print(f"The hypotenuse is {h}.")
