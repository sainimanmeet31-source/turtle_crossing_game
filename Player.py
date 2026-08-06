from turtle import Turtle

class player(Turtle):
    def __init__(self):
        super().__init__()
        self.create()
    def move(self):
        self.forward(20)
    def create(self):
        self.penup()
        self.color('black')
        self.shape('turtle')
        self.setheading(90)
        self.goto(0,-280)
        self.speed('fastest')
        
