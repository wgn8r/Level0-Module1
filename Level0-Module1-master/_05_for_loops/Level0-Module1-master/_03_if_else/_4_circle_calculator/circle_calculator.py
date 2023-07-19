# Write a Python program that asks the user for the radius of a circle.
# Next, ask the user if they would like to calculate the area or circumference of a circle.
# If they choose area, display the area of the circle using the radius.
# Otherwise, display the circumference of the circle using the radius.
import math
#Area = πr^2
#Circumference = 2πr
rad=input("what do you want the radius to be?")
rad=int(rad)
ac=input("area or circumference of a circle")
if ac=="area":
    print(math.pi*rad*rad)
elif ac=="circumference":
    print(math.pi*2*rad)
