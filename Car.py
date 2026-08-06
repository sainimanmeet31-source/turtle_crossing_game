from turtle import Turtle
import random
c=['purple','black','blue','green','yellow','orange','red']

class car(Turtle):
    def __init__(self):
        super().__init__()
        self.new()
    def move(self):
        self.forward(10)
    def new(self):
        self.penup()
        self.color(random.choice(c))
        self.shape('square')
        self.shapesize(1,2)
        self.speed('slowest')
        self.goto(280,random.randrange(-260,260,20))
        self.setheading(180)
    def clean(self):
        self.clear()
        
