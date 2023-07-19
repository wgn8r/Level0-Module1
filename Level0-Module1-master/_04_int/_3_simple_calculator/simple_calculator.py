"""
* Write a Python program that asks the user for two numbers.

* Then ask the user if the would like to add, subtract, multiply, or divide.

* Use if-else statements to provide the desired math operation on the numbers
  and display the result.
"""
choice=input("add, subtract, multiply, or divide")
a=input()
int(a)

b=input()
int(b)


def add(a, b):
        print(int(a) + int(b))
def mult(a,b):
        print (int(a)*int(b))
def sub(a,b):
        print (int(a)-int(b))
def div(a,b):
        print (int(a)/int(b))
if choice=="add":
    add(a, b)

if choice=="multiply":
    mult(a, b)

if choice=="sub":
    sub(a, b)

if choice=="divide":
    div(a, b)
