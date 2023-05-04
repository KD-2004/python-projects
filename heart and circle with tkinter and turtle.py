import turtle
import tkinter as tk

root = tk.Tk()

canvas = turtle.Canvas(root, height=1000, width=1000)
canvas.pack()

# Create the RawTurtle object
t = turtle.RawTurtle(canvas)
t.hideturtle()
t.penup()
t.goto(0, -100)
t.pendown()

def heart():
    # Clear any previous drawings
    t.clear()

    # Draw the heart
    t.begin_fill()
    t.color("red")
    t.left(130)
    t.forward(280)
    t.circle(-170, 200)
    t.setheading(60)
    t.circle(-170, 200)
    t.forward(390)
    t.right(90)
    t.forward(300)
    t.end_fill()

def circle():
    # Clear any previous drawings
    t.clear()
    t.fillcolor("blue")
    t.begin_fill()
    # Draw the circle
    t.circle(100)
    t.end_fill()
# Create the buttons
heart_button = tk.Button(root, text="Heart", command=heart)
heart_button.pack()

circle_button = tk.Button(root, text="Circle", command=circle)
circle_button.pack()

root.mainloop()





