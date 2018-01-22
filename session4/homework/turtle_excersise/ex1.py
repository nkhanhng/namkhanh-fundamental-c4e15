from turtle import *

def draw_poly(n,col,fw,lf):
    for i in range(n):
        color(col)
        forward(fw)
        left(lf)

shape("turtle")
speed(0)
colors = ['red', 'blue', 'brown', 'yellow', 'grey']

triangle = draw_poly(3,colors[0],100,120)

square = draw_poly(4,colors[1],100,90)

pentagon = draw_poly(5,colors[2],100,72)

hexagon = draw_poly(6,colors[3],100,60)

heptagon = draw_poly(7,colors[-1],100,51)


mainloop()
