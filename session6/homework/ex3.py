from turtle import *

def draw_square(lgth,col):
    for i in range(4):
        color(col)
        forward(lgth)
        right(90)

shape("turtle")

draw_square(100,"red")

mainloop()
