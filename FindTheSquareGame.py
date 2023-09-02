import turtle
import random

#CONSTANTS
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
SQUARE_STRETCH = 10

#Screen
win = turtle.Screen()
win.title("Find the Square!")
win.bgcolor("light blue")
win.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
win.tracer(0)
win.colormode(255)

#Square
square = turtle.Turtle()
square.shape("square")
square.shapesize(stretch_wid=SQUARE_STRETCH, stretch_len=SQUARE_STRETCH)
square.color("light blue")
square.penup()
square.x = random.randint((SQUARE_STRETCH*20) - (SCREEN_WIDTH//2), (SCREEN_WIDTH//2) - (SQUARE_STRETCH*20))
square.y = random.randint((SQUARE_STRETCH*20) - (SCREEN_HEIGHT//2), (SCREEN_HEIGHT//2) - (SQUARE_STRETCH*20))
square.goto(square.x, square.y)

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.penup()
pen.hideturtle()

#Turtle
turt = turtle.Turtle()
#turt.shapesize(stretch_wid=3, stretch_len=3)
turt.speed(0)
turt.shape("turtle")
turt.color("light green")
turt.penup()

#Functions
def move_right():
    turt.tiltangle(360)
    x = turt.xcor()
    x += 10
    turt.setx(x)

def move_left():
    turt.tiltangle(180)
    x = turt.xcor()
    x -= 10
    turt.setx(x)

def move_up():
    turt.tiltangle(90)
    y = turt.ycor()
    y += 10
    turt.sety(y)

def move_down():
    turt.tiltangle(270)
    y = turt.ycor()
    y -= 10
    turt.sety(y)

def win_game():
    square.color("dark blue")

    pen.goto(square.x, square.y + 150)
    pen.color("dark blue")
    pen.write("YOU WIN!", align = "center", font = ("Courier", 15, "normal"))

    turt.color("white")


#Keyboard Binding
win.listen()
win.onkeypress(move_right, "Right")
win.onkeypress(move_left, "Left")
win.onkeypress(move_up, "Up")
win.onkeypress(move_down, "Down")
win.onkeypress(win_game, "Return")

#MAIN
while True:
    win.update()

    square_half = (SQUARE_STRETCH*20) // 2

    if turt.xcor() > square.x - square_half and turt.xcor() < square.x + square_half and turt.ycor() > square.y - square_half and turt.ycor() < square.y + square_half:
        color1 = random.randint(0,250)
        color2 = random.randint(0,250)
        color3 = random.randint(0,250)
        turt.color(color1, color2, color3)
    else:
        turt.color(255, 255, 255)

