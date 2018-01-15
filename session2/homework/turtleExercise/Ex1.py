from turtle import *

shape("turtle")
color("red")
speed(0)
pensize(5)

for j in range(2):
    for i in range(2):
        left(20)
        forward(100)
        right(30)
        forward(100)
        right(150)
        forward(100)
        right(30)
        forward(100)

    right(72)



mainloop()
