from turtle import Turtle

class scoreboard(Turtle):
    def __init__(self):
        super().__init__()

        self.score = 0
        self.color("blue")  # Set the color attribute
        self.hideturtle()
        self.penup()
        self.goto(0, 260)  # Set the position before writing the score
        self.update_score()
        

    def update_score(self):
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))


    def gameOver(self):
        self.goto(0,0)
        self.color("white")
        self.write(f"GAME OVER", align="center", font=("Arial", 24, "normal"))

    def inc_score(self):
        self.score+=1
        self.clear()
        self.update_score()
