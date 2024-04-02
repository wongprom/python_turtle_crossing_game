from turtle import Turtle, Screen
import time
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Screen
screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)
# Turtle
t = Turtle()
screen.exitonclick()


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()