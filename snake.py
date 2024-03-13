from turtle import Turtle
POSITIONS=[(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE=20


class snake():
    def __init__(self):
        self.segment=[]
        self.create_snake()
        #self.head is the head of the snake
        self.head=self.segment[0]

    def create_snake(self):
        for turtle_positions in POSITIONS:
            turtle1=Turtle("square")
            turtle1.penup()
            turtle1.color("white")
            turtle1.goto(turtle_positions)
            self.segment.append(turtle1) #add each segmnet to the list
#moving the snake
    def snake_move(self):
            for seg in range(len(self.segment)-1,0,-1):
                new_x=self.segment[seg-1].xcor()
                new_y=self.segment[seg-1].ycor()
                self.segment[seg].goto(new_x,new_y)
            self.head.forward(MOVE_DISTANCE) 

#taking keystrokes fro keyboard
    def right(self):
        self.head.setheading(0)
    def up(self):
        self.head.setheading(90)
    def left(self):
        self.head.setheading(180)
    def down(self):
        self.head.setheading(270)
    
