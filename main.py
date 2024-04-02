from turtle import Screen
import time
from player import Player
from car_manager import CarManager
# from scoreboard import Scoreboard

# Screen
screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)

# Turtle
t = Player()

# Move turtle
screen.listen()
screen.onkey(t.go_up, "Up")

# Car
car_manager = CarManager()


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

screen.exitonclick()
