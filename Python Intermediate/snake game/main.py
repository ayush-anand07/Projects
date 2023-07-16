
from food import Food
from turtle import  Screen
import time
from snake import Snake
from scoreboard import ScoreBoard
screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

scoreboard.update_scoreboard()
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)                 #---------------------> refresh screen every 0.1 sec
    snake.move()
    
    
    if snake.segments[0].distance(food) < 15:
        food.refresh()
        scoreboard.update_score()
        scoreboard.update_scoreboard()
        snake.increse_length()

    if snake.segments[0].xcor()> 300 or snake.segments[0].xcor() < -300 or snake.segments[0].ycor()> 300 or snake.segments[0].ycor() < -300:
        scoreboard.reset()
        snake.reset()
   

    # detect collosion with tail

    for segments in snake.segments:
        if segments == snake.segments[0]:
            pass

        elif snake.segments[0].distance(segments) < 10:
            
            scoreboard.reset()
            snake.reset()




screen.exitonclick()

