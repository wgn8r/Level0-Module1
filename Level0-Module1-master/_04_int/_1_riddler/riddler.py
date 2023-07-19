"""
* Write a python program that asks the user a minimum of 3 riddles.

* You can look at riddles.com if you don't already know any riddles.

* Collect the response of each riddle from the user and compare their
  answers to the correct answer. 

* Use a variable to keep track of the correctly answered riddles

* After all the riddles have been asked, tell the user how many they got
  correct
"""
score=0
x1=input("The more you take, the more you leave behind.")
if x1=="footsteps":
    score+=1
x2=input("What has a head, a tail, is brown, and has no legs?")
if x2=="a penny":
    score+=1
x3=input("David's father has three sons: Snap, Crackle, and _____?")
if x3=="david":
    score+=1
print(score)
