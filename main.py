from turtle import Turtle,Screen
import time
from snake import snake
from food import food
from scoreboard import scoreboard
screen=Screen()

#1-:setting upthe environment....
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("SNAKE GAME")
screen.tracer(0)


#All snake class object..
snake=snake()
food=food()
scoreboard = scoreboard()

#taking keystrokes fro keyboard
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

moving = True
while moving:
    screen.update()
    time.sleep(0.1)
    snake.snake_move()

    #to check if food is collieded to the snake...
    if snake.head.distance(food)<15:    #if the snake head is 15 pixels from the food
        food.random_food()
        scoreboard.inc_score()
    
    #collison with wall..
    if snake.head.xcor()>280 or snake.head.xcor()< -280 or snake.head.ycor()>280 or snake.head.ycor()< -280:
        moving=False
        scoreboard.gameOver()
    

            
screen.exitonclick()