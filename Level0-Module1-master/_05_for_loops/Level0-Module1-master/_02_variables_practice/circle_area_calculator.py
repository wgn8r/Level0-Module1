import turtle
from tkinter import messagebox, simpledialog, Tk
import math

# Goal: Write a Python program that asks the user for the radius 
#       of a circle and displays the area of that circle.
#       The formula for the area of a circle is πr^2.
#       See example image in package to check your output.

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    # Ask the user for the radius in pixels and store it in a variable
    rad=simpledialog.askinteger(title= None, prompt="give me a radius")
    
    # Make a new turtle
    x=turtle.Turtle()
    x.circle(radius=rad)
    x.penup()
    x.goto(89,12)
    area=math.pi*rad**2

    # Have your turtle draw a circle with the correct radius
    # my_turtle.circle()

    # Call the turtle .penup() method

    # Move your turtle to a new x,y position using .goto()

    # Calculate the area of your circle and store it in a variable
    # Hint, you can use math.pi
    
    # Write the area of your circle using the turtle .write() method
    # my_turtle.write(arg="area = " + str(area), move=True, align='left', font=('Arial',8,'normal'))
    x.write(arg="area=" + str(area), move=True, align='left', font=('Arial',20,'normal'))
    # Hide your turtle
    x.hideturtle()
    turtle.done()

    # Call turtle.done()
