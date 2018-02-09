from turtle import *

def draw_star(x,y,lgth):
    penup()
    setposition(x,y)
    pendown()
    for i in range(5):
        forward(lgth)
        right(144)

shape('turtle')


draw_star(200,50,100)

mainloop()
