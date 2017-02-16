from turtle import *
right(15)
color("red")
speed(-1)
for i in range (4):
    for j in range (2):
        forward(100)
        left (30)
        forward(100)
        if j%2==0:
            left(150)
        else:
            right(120)
left(120)
    
