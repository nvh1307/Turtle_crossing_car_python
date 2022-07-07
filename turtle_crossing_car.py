import time
from turtle import Turtle,Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


sc = Screen()
sc.setup(width=600,height=600)
sc.tracer(0)
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
sc.listen()
sc.onkey(player.goup,"Up")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    sc.update()
    car_manager.create_car()
    car_manager.move_cars()
    # detect
    for car in car_manager.all_cars:
        if car.distance(player)<20:
            game_is_on = False
            scoreboard.game_over()
    # detect finish 
    if player.is_at_finish_line():
        player.gotostart()
        car_manager.level_up()
        scoreboard.increase_level()
        scoreboard.update_scoreboard()



sc.exitonclick()
