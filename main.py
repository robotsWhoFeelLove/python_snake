from turtle import Screen, Turtle
from snake import Snake
from food import Food
import time
from scoreboard import Scoreboard



def main():

    screen = Screen()
    screen.setup(width= 600, height = 600)
    screen.bgcolor("black")
    screen.title("Python Snake")
    screen.tracer(0)


    snake = Snake()

    screen.update()
    sleep_time = 0.1
    distance = 20


    # def move_snake():

    def new_game():
        snake.reset_snake()
        scoreboard.reset_scoreboard()



    def turn_up():
        snake.set_dir(90)
    def turn_down():
        snake.set_dir(270)
    def turn_left():
        snake.set_dir(180)
    def turn_right():
        snake.set_dir(0)


    food = Food()


    screen.listen()
    screen.onkeypress(fun=turn_up, key="Up" )
    screen.onkey(key="Down", fun=turn_down)
    screen.onkey(key="Left", fun=turn_left)
    screen.onkey(key="Right", fun=turn_right)

    scoreboard = Scoreboard()

    game_is_on = True
    while game_is_on:
        snake.move()
        screen.update()
        time.sleep(sleep_time)

        #detect colission
        if snake.head.distance(food) < 15:
            scoreboard.increment()
            food.refresh()
            snake.eat_food()

        # check for wall
        if snake.check_wall() or snake.check_tail():
            scoreboard.reset_scoreboard()
            snake.reset_snake()
            snake.move()


    screen.exitonclick()

main()