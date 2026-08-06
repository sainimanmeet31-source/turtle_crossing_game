from turtle import Turtle

class Level(Turtle):
    def __init__(self):
        super().__init__()
        count=1
        self.ht()
        self.penup()
        self.color('black')
        self.goto(-300,250)
        self.write(f'Level {count}:',font=('Arial',15,'normal'))
    def level_up(self,a):
        self.clear()
        self.write(f'Level {a}:',font=('Arial',15,'normal'))
        
