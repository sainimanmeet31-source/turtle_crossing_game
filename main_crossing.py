import turtle
import random
from level import Level
from Player import player
from Car import car
import time
screen=turtle.Screen()
screen.screensize(600,600)
screen.tracer(0)
l=Level()
p1=player()
screen.listen()
screen.onkey(p1.move,'Up')
game_is_on=True
count=1
cars=[]
cars.append(car())
a=0.1
while game_is_on:
    screen.update()
    time.sleep(a)
    if random.randint(1,3) == 1:
        new_car= car()
        cars.append(new_car)
    if p1.ycor()==280:
        count+=1
        p1.clear()
        p1.create()
        l.level_up(count)
        a=a*(0.6)
    for c in cars:
        c.move()
        if p1.distance(c)<10:
            l.goto(-50,0)
            l.write('Game over',font=('Arial',15,'normal'))
            game_is_on=False
        elif c.xcor()<=-280:
            c.hideturtle()
            cars.remove(c)

screen.exitonclick()
