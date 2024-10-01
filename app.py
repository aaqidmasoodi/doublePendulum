import turtle
import math

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Double Pendulum Simulation")
screen.setup(width=800, height=600)

# Turn off automatic screen updates to make the animation smooth
screen.tracer(0, 0)

# Parameters for the pendulum
G = 1  # Gravitational constant
L1 = 200  # Length of the first pendulum arm
L2 = 200  # Length of the second pendulum arm
M1 = 10   # Mass of the first pendulum
M2 = 10   # Mass of the second pendulum

# Initial angles (in radians)
a1 = math.pi / 2
a2 = math.pi / 2

# Initial angular velocities
a1_v = 0
a2_v = 0

# Turtle object for drawing pendulum arms
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.width(2)

# Turtle for tracing the pendulum path
trace = turtle.Turtle()
trace.hideturtle()
trace.speed(0)
trace.width(1)
trace.penup()

# Function to update pendulum positions and angles
def update_positions():
    global a1, a2, a1_v, a2_v
    
    # Equations of motion for double pendulum
    num1 = -G * (2 * M1 + M2) * math.sin(a1)
    num2 = -M2 * G * math.sin(a1 - 2 * a2)
    num3 = -2 * math.sin(a1 - a2) * M2
    num4 = a2_v ** 2 * L2 + a1_v ** 2 * L1 * math.cos(a1 - a2)
    den = L1 * (2 * M1 + M2 - M2 * math.cos(2 * a1 - 2 * a2))
    a1_a = (num1 + num2 + num3 * num4) / den
    
    num1 = 2 * math.sin(a1 - a2)
    num2 = (a1_v ** 2 * L1 * (M1 + M2) + G * (M1 + M2) * math.cos(a1) + a2_v ** 2 * L2 * M2 * math.cos(a1 - a2))
    den = L2 * (2 * M1 + M2 - M2 * math.cos(2 * a1 - 2 * a2))
    a2_a = num1 * num2 / den
    
    # Update angular velocities and angles
    a1_v += a1_a
    a2_v += a2_a
    a1 += a1_v
    a2 += a2_v

# Function to draw the double pendulum
def draw_pendulum():
    pen.clear()  # Clear the previous pendulum frame
    
    x1 = L1 * math.sin(a1)
    y1 = -L1 * math.cos(a1)
    
    x2 = x1 + L2 * math.sin(a2)
    y2 = y1 - L2 * math.cos(a2)
    
    pen.penup()
    pen.goto(0, 0)  # Starting point (pivot)
    pen.pendown()
    
    pen.goto(x1, y1)  # Draw the first arm
    pen.goto(x2, y2)  # Draw the second arm
    
    # Trace the path of the second pendulum
    trace.goto(x2, y2)
    trace.pendown()

# Main loop to update and draw the pendulum
def simulate():
    update_positions()
    draw_pendulum()
    screen.update()  # Update the screen with new drawing
    screen.ontimer(simulate, 10)  # Set a small delay for smooth animation

simulate()
turtle.done()
