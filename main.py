from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Scoreboard
import time

# Create screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)  # Turn off the animation

# Create ball
ball = Ball()

# Create paddles

r_paddle = Paddle((380, 0))
l_paddle = Paddle((-380, 0))

# create score board
scoreboard = Scoreboard()

# Make paddle up and down

screen.listen()
screen.onkeypress(r_paddle.move_up, 'Up')
screen.listen()
screen.onkeypress(r_paddle.move_down, 'Down')
screen.listen()
screen.onkeypress(l_paddle.move_up, 'w')
screen.listen()
screen.onkeypress(l_paddle.move_down, 's')

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()  # Para que se vea la animacion en pantalla
    ball.move()

    # Bounce against the walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # bounce against the paddles
    if ball.distance(l_paddle) < 50 and ball.xcor() < -360:
        ball.bounce_x()
        scoreboard.r_point()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 360:
        ball.bounce_x()
        scoreboard.l_point()

    # Detect when ball is off canvas
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.r_point()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.l_point()

screen.exitonclick()
