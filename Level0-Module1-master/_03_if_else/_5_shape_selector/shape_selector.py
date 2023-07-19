import turtle
from tkinter import messagebox, simpledialog, Tk

# Goal: Write a Python program that asks the user whether they want to
#       draw a triangle, square, or circle and then draw that shape.

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    
    # Make a new turtle
    x=turtle.Turtle()
    x.speed(1)
    shape=input("what shape do you want:triangle, square, or circle")
    if shape=="circle":
        x.circle(30)
    elif shape=="triangle":
        x.forward(30)
        x.right(120)
        x.forward(30)
        x.right(120)
        x.forward(30)
        x.right(120)
    elif shape =="square":
        x.forward(60)
        x.right(90)
        x.forward(60)
        x.right(90)
        x.forward(60)
        x.right(90)
        x.forward(60)
        x.right(90)
    turtle.done

    # Ask the user what shape they want to draw and store it in a variable
    
    # Draw the shape requested by the user using if-elif-else statements
    
    # Call the turtle .done() method
