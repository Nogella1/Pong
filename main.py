
# https://www.youtube.com/watch?v=C6jJg9Zan7w&ab_channel=freeCodeCamp.org
# C:\Users\legon\AppData\Local\Programs\Python\Python310\python.exe

import time # time functions
import turtle  # simple graphics / game engine
import winsound     # to play sounds
import random       # to vary things a bit

frame_time = 0.02   # 50 frames per second

# scores
left = 0
right = 0

#new stuff
#print(time.time())
#winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
#winsound.PlaySound("ding.wav", winsound.SND_ASYNC)
#print(random.uniform(0.7, 1.3))
#quit()

# set up the screen
wn = turtle.Screen()   # a window for the game
wn.title("PONG Game")
wn.bgcolor("white")  # black white pink all OK
wn.setup(width=800, height=600)  # size of window  0,0 is at the centre
wn.tracer(0)  # stops screen updating itself

# set up the pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.clear()
pen.write(f"{left}  :  {right}",align="center", font=("Arial", 24, "bold"))

# Left Paddle pad_L
pad_L = turtle.Turtle()  # Turtle is a class of the turtle module
pad_L.speed(0)  # this is the fastest possible speed
pad_L.shape("square")  # will be a rectangle
pad_L.shapesize(stretch_wid=5, stretch_len=1)  # 5 times as high as it is wide
pad_L.color("pink")
pad_L.penup()  # don't want it to draw lines
pad_L.goto(-350, 0)  # mid screen at the left hand side

# Right Paddle pad_R
pad_R = turtle.Turtle()  # Turtle is a class of the turtle module
pad_R.speed(0)  # this is the fastest possible speed
pad_R.shape("square")  # will be a rectangle
pad_R.shapesize(stretch_wid=5, stretch_len=1)  # 5 times as high as it is wide
pad_R.color("black")
pad_R.penup()  # don't want it to draw lines
pad_R.goto(350, 0)  # mid screen at the left hand side

# Ball  ball
ball = turtle.Turtle()  # Turtle is a class of the turtle module
ball.speed(0)  # this is the fastest possible speed
ball.shape("circle")
ball.color("red")
ball.penup()  # don't want it to draw lines
ball.goto(0, 0)  # mid screen at the left hand side
ball.dx = 3     # ball x-movement each frame
ball.dy = 3     # ball y-movement each frame

# Paddle Functions
def upL():
    y = pad_L.ycor()
    y += 20
    pad_L.sety(y)

def downL():
    y = pad_L.ycor()
    y -= 20
    pad_L.sety(y)

def upR():
    y = pad_R.ycor()
    y += 20
    pad_R.sety(y)

def downR():
    y = pad_R.ycor()
    y -= 20
    pad_R.sety(y)

def quit_game():
    wn.bye()

def check_border():
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        ball.dy *= 1.05
        ball.dx *= 1.05
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        ball.dy *= 1.05
        ball.dx *= 1.05
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

def check_score():
    global left
    global right
    if ball.xcor() > 390 or ball.xcor() < -390:
        if ball.xcor() > 390:
            left += 1
        else:
            right += 1
        pen.clear()
        pen.write(f"{left}  :  {right}", align="center", font=("Arial", 24, "bold"))
        winsound.PlaySound("ding.wav", winsound.SND_ASYNC)
        if left > 4 or right > 4:
            time.sleep(0.5)
            quit()
        ball.goto(0, 0)
        ball.dx *= -1

        if random.randint(0, 1) == 0:
            ball.dy *= -1  # Reverse the Y movement
        if ball.dx > 0:  # LEFT or RIGHT
            ball.dx = 3
        else:
            ball.dx = -3

        if ball.dy > 0:  # UP or DOWN
            ball.dy = 3
        else:
            ball.dy = -3
        pad_L.sety(0)
        pad_R.sety(0)

        delay = True  # Wait a bit

def check_paddles():
    adjust = random.uniform(0.8, 1.2)       # random between 0.8 & 1.2 so bounce not predictable
    if (ball.xcor() > 330 and ball.xcor() < 350) and (ball.ycor() < pad_R.ycor() + 50 and ball.ycor() > pad_R.ycor() -50):
        ball.setx(330)
        ball.dx *= -1                       # reverse the x direction
        ball.dy *= adjust                   # adjusted y movement
    if (ball.xcor() < -330 and ball.xcor() > -350 ) and (ball.ycor() < pad_L.ycor() + 50 and ball.ycor() > pad_L.ycor() -50):
        ball.setx(-330)
        ball.dx *= -1
        ball.dy *= adjust
# moving paddles
# Keyboard binding
wn.listen()
wn.onkeypress(upL, "w")
wn.onkeypress(downL, "s")
wn.onkeypress(upR, "Up")
wn.onkeypress(downR, "Down")
wn.onkeypress(quit_game, "q")

if random.randint(0,1) == 0:    # randomise which way the game starts
    ball.dy *= -1
if random.randint(0,1) == 0:
    ball.dx *= -1

delay = True        # slight pause before we start
frame = 0           # seconds so far in this frame
start = time.time() # number of seconds at start of game  ****

# Main game loop
while True:         # loop until we tell it to stop
    now = time.time()
    frame = now - start

    if frame > 0.02:    # new frame starts here
        start = now
        wn.update()    # update the screen
        if delay:
            pad_L.sety(0)
            pad_R.sety(0)

            time.sleep(0.5)
            delay = False
            start = time.time()
        ball.setx(ball.xcor() + ball.dx)    # move the ball by dx
        ball.sety(ball.ycor() + ball.dy)    # move the ball by dy

        check_border()      # Border checking
        check_score()       # Check for score
        check_paddles()     # check the paddles

quit()



