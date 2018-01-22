from turtle import *

def draw_rectangle(m,n):
    for i in range(2):
        forward(m)
        left(90)
        forward(n)
        left(90)

shape("turtle")
speed(1)

colors = ['red', 'blue', 'brown', 'yellow', 'grey']
for j in colors:
    color(str(j))
    begin_fill()
    draw_rectangle(50,100)
    forward(50)
    end_fill()


mainloop()
