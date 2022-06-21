
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

'''# set up the pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.clear()
pen.write(f"{left}  :  {right}",align="center", font=("Arial", 24, "normal"))'''

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
    pad_R.sety(400)

# Keyboard binding
wn.listen()
wn.onkeypress(upL, "w")
wn.onkeypress(downL, "s")
wn.onkeypress(upR, "Up")
wn.onkeypress(downR, "Down")
#wn.onkeypress(quit_game, "q")

delay = True
frame = 0
start = time.time() # number of seconds at start of game  ***********

# Main game loop
while True:         # loop until we tell it to stop
    now = time.time()
    frame = now - start

    if frame > 0.02:
        start = now
        wn.update()    # we control when it updates
        if delay:
            time.sleep(0.5)
            delay = False
            start = time.time()
        #if pad_R.ycor()>350:
            #quit()
        ball.setx(ball.xcor() + ball.dx)    # move the ball by dx
        ball.sety(ball.ycor() + ball.dy)    # move the ball by dy

        # Top Border checking
        if ball.ycor() > 290:
            ball.sety(290)
            ball.dy *= -1
            ball.dy *= 1.1
            ball.dx *= 1.1
        elif ball.ycor() < -290:
            ball.sety(-290)
            ball.dy *= -1
            ball.dy *= 1.1
            ball.dx *= 1.1

        # Check for score
        if ball.xcor()> 390 or ball.xcor()< -390:
            if ball.xcor() > 390:
                left += 1
            else:
                right += 1
            #pen.clear()
            #pen.write(f"{left}  :  {right}",align="center", font=("Arial", 24, "normal"))
            if left > 4 or right > 4:
                quit()
            ball.goto(0,0)
            ball.dx *= -1
            if ball.dx > 0:
                ball.dx = 3
            else:
                ball.dx = -3
            if ball.dy > 0:
                ball.dy = 3
            else:
                ball.dy = -3

            delay = True

            # check the paddles
        if (ball.xcor() > 330 and ball.xcor() < 350) and (ball.ycor() < pad_R.ycor() + 50 and ball.ycor() > pad_R.ycor() -50):
            ball.setx(330)
            ball.dx *= -1
        if (ball.xcor() < -330 and ball.xcor() > -350 ) and (ball.ycor() < pad_L.ycor() + 50 and ball.ycor() > pad_L.ycor() -50):
            ball.setx(-330)
            ball.dx *= -1

        #time.sleep(0.02)



