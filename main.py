# https://www.youtube.com/watch?v=C6jJg9Zan7w&ab_channel=freeCodeCamp.org
# C:\Users\legon\AppData\Local\Programs\Python\Python310\python.exe

import time # time functions
import turtle  # simple graphics / game engine
import winsound     # to play sounds
import random       # to vary things a bit

frame_rate = 50             # 50 fps
frame_time = 1/frame_rate   # 20 msec
stop_game = False           # quit

left = 0    # Left player score
right = 0   # Right player score

# set up the screen
wn = turtle.Screen()   # a window for the game
wn.title("PONG Game")
wn.bgcolor("purple")  # black white pink all OK
wn.setup(width=800, height=600, startx= None, starty= 5)  # size of window
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

pad_L = turtle.Turtle()  # Turtle is a class of the turtle module
pad_L.speed(0)  #  fastest possible drawing speed
pad_L.shape("square")  # will be a rectangle
pad_L.shapesize(stretch_wid=5, stretch_len=1)  # 5 times as high as it is wide
pad_L.color("pink")
pad_L.penup()  # don't want it to draw lines
pad_L.goto(-350, 0)  # mid screen at the left hand side
pad_L.dy = 0        # amount to move up or down
# Right Paddle pad_R
pad_R = turtle.Turtle()  # Turtle is a class of the turtle module
pad_R.speed(0)  # this is the fastest possible speed
pad_R.shape("square")  # will be a rectangle
pad_R.shapesize(stretch_wid=5, stretch_len=1)  # 5 times as high as it is wide
pad_R.color("black")
pad_R.penup()  # don't want it to draw lines
pad_R.goto(350, 0)  # mid screen at the left hand side
pad_R.dy = 0        # amount to move up or down

class Ball(turtle.Turtle):
    def __init__(self):
        super().__init__()
        #ball = turtle.Turtle()  # Turtle is a class of the turtle module
        self.speed(0)  # this is the fastest possible speed
        self.shape("circle")
        self.color("red")
        self.penup()  # don't want it to draw lines
        self.goto(0, 0)  # mid screen at the left hand side
        self.dx = 3     # ball x-movement each frame
        self.dy = 3     # ball y-movement each frame
ball = Ball()

'''
ball = turtle.Turtle()
ball.speed(0)  # this is the fastest possible speed
ball.shape("circle")
ball.color("red")
ball.penup()  # don't want it to draw lines
ball.goto(0, 0)  # mid screen at the left hand side
ball.dx = 3     # ball x-movement each frame
ball.dy = 3     # ball y-movement each frame
'''
# Paddle Functions
def upL():
    pad_L.dy = 6
def downL():
    pad_L.dy = -6
def stopL_Up():
    if pad_L.dy > 0:
        pad_L.dy = 0
def stopL_Down():
    if pad_L.dy < 0:
        pad_L.dy = 0
def upR():
    pad_R.dy = 6
def downR():
    pad_R.dy = -6
def stopR_Up():
    if pad_R.dy > 0:
        pad_R.dy = 0
def stopR_Down():
    if pad_R.dy < 0:
        pad_R.dy = 0

def quit_game():
    global stop_game
    stop_game = True

def move_paddles():
    pad_R.sety(pad_R.ycor() + pad_R.dy)  # move Right paddle
    if abs(pad_R.ycor()) > 300:
        pad_R.sety(pad_R.ycor() - pad_R.dy)
    pad_L.sety(pad_L.ycor() + pad_L.dy)  # move Left paddle
    if abs(pad_L.ycor()) > 300:
        pad_L.sety(pad_L.ycor() - pad_L.dy)

def check_border():
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        ball.dy *= 1.05
        ball.dx *= 1.05
        pad_R.dy *= 1.05
        pad_L.dy *= 1.05
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        ball.dy *= 1.05
        ball.dx *= 1.05
        pad_R.dy *= 1.05
        pad_L.dy *= 1.05
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

def check_score():
    global left, right, start_up

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

        start_up = True  # Wait a bit

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

# Keyboard binding
wn.listen()
wn.onkeypress(upL, "w")
wn.onkeyrelease(stopL_Up, "w")
wn.onkeypress(downL, "s")
wn.onkeyrelease(stopL_Down, "s")

wn.onkeypress(upR, "Up")
wn.onkeyrelease(stopR_Up, "Up")
wn.onkeypress(downR, "Down")
wn.onkeyrelease(stopR_Down, "Down")

wn.onkeypress(quit_game, "q")

#  *******************************

# Randomise which way the game starts
if random.randint(0,1) == 0:
    ball.dy *= -1
if random.randint(0,1) == 0:
    ball.dx *= -1

start_up = True        # slight pause before we start
frame_so_far = 0           # seconds so far in this frame
start_time = time.time() # number of seconds at start of game  ****

# Main game loop  **************
while True:         # loop until we tell it to stop
    now = time.time()
    frame_so_far = now - start_time

    if frame_so_far > frame_time:    # new frame starts here
        start_time = now
        wn.update()    # update the screen
        if start_up:
            time.sleep(0.5)
            start_up = False
            start_time = time.time()

        ball.setx(ball.xcor() + ball.dx)    # move the ball by dx
        ball.sety(ball.ycor() + ball.dy)    # move the ball by dy

        move_paddles()      # Move the paddles
        check_border()      # Border checking
        check_score()       # Check for a score
        check_paddles()     # check the paddles

        if stop_game:
            break

quit()



