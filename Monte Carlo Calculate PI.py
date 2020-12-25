import random
import turtle

numOfall=100
numOfaim=0
turtle.hideturtle()
turtle.penup() 
turtle.goto(0,-50)
turtle.pendown()
turtle.circle(50)
turtle.penup()

for i in range(numOfall):
    x=random.random()*2-1
    y=random.random()*2-1
    turtle.goto(x*50,y*50)
    turtle.pendown()
    turtle.dot(4,"black")
    turtle.penup()  
    if x*x+y*y<=1:
        numOfaim+=1

pi=4*numOfaim/numOfall
print("pi is",pi)
