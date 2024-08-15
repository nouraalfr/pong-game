import turtle
import os

wn = turtle.Screen()
wn.title("Simple Cute Pong Game")
wn.bgcolor("black")
wn.setup(800, 600)
wn.tracer(0)

score_a = 0
score_b = 0

# Paddle A
paddleA = turtle.Turtle()
paddleA.speed(0)
paddleA.shape("square")
paddleA.color("red")
paddleA.penup()
paddleA.goto(-350, 0)
paddleA.shapesize(5, 1)
# Paddle B
paddleB = turtle.Turtle()
paddleB.speed(0)
paddleB.shape("square")
paddleB.color("red")
paddleB.penup()
paddleB.goto(350, 0)
paddleB.shapesize(5, 1)
# Ballx
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("blue")
ball.penup()
ball.shapesize(1.75, 1.5)
ball.goto(0, 0)
ball.dx = 3
ball.dy = -3
# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("pink")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write(
    "Player A: 0        Player B: 0 ", align="center", font=("Courier", 26, "bold")
)


# paddle A
def paddleA_up():
    y = paddleA.ycor()
    y += 20
    paddleA.sety(y)


def paddleA_down():
    y = paddleA.ycor()
    y -= 20
    paddleA.sety(y)


# paddle B
def paddleB_up():
    y = paddleB.ycor()
    y += 20
    paddleB.sety(y)


def paddleB_down():
    y = paddleB.ycor()
    y -= 20
    paddleB.sety(y)


# keyboard binding
wn.listen()
wn.onkeypress(paddleA_up, "q")
wn.onkeypress(paddleA_down, "z")
wn.onkeypress(paddleB_up, "Up")
wn.onkeypress(paddleB_down, "Down")

while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking for up and down using y coordinate
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        os.system("afplay bounce.wav&")

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        os.system("afplay bounce.wav&")

    # Border checking for left and right using x coordinate
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1

        score_a += 1
        pen.clear()
        pen.write(
            "Player A: {}       Player B: {} ".format(score_a, score_b),
            align="center",
            font=("Courier", 26, "bold"),
        )

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write(
            "Player A: {}       Player B: {} ".format(score_a, score_b),
            align="center",
            font=("Courier", 26, "bold"),
        )

    # boucing ball by paddle
    if (ball.xcor() > 340 and ball.xcor() < 350) and (
        ball.ycor() < paddleB.ycor() + 40 and ball.ycor() > paddleB.ycor() - 40
    ):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (
        ball.ycor() < paddleA.ycor() + 40 and ball.ycor() > paddleA.ycor() - 40
    ):
        ball.setx(-340)
        ball.dx *= -1
