from turtle import *

def draw_square(lgth,col):
    for i in range(4):
        color(col)
        forward(lgth)
        right(90)

shape("turtle")
speed(0)

for i in range(30):
    draw_square(i * 5, 'red')
    left(17)
    penup()
    forward(i * 2)
    pendown()

mainloop()
