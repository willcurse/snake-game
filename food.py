from turtle import Turtle
import random

class food(Turtle):
    def __init__(self):
        super().__init__()

        self.shape("turtle")
        self.penup()
        self.shapesize(0.9,0.9)
        self.color("red")
        self.speed("fastest")
        self.random_food()

#appering food to randomly..        
    def random_food(self):
        random_x=random.randint(-280,280)
        random_y=random.randint(-280,280)
        self.goto(random_x,random_y)




        