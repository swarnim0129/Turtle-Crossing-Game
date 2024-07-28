from turtle import Turtle

FONT = ("Courier", 24, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("black")
        self.level=1

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center",font=FONT)

    def level_up(self):
        self.clear()
        self.goto(-220,250)
        self.write(f'LEVEL :{self.level}',align="center",font=FONT)
        self.level+=1



