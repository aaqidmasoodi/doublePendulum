import turtle
import math


# Screen
win = turtle.Screen()
win.setup(width=800, height=600)
win.bgcolor('lightblue')
win.title('Double Pendulum')



# First Pendulum
top_pendulum = turtle.Turtle()
top_pendulum.shape('square')
top_pendulum.penup()
top_pendulum.shapesize(stretch_wid=1, stretch_len=10)
top_pendulum.color('#402f00')
top_pendulum.angle = 0
top_pendulum.acceleration = 10



while True:

    top_pendulum.setheading(top_pendulum.angle)

    
    if top_pendulum.heading() > 180:
        top_pendulum.acceleration *= -1

    top_pendulum.angle += top_pendulum.acceleration
    
    

    win.update()