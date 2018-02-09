from random import randint,choice
from calc import eval

a = randint(0,10)
b = randint(0,10)
error = randint(-1,1)

op_list = ["+","-","*","/"]
op = choice(op_list)

display_result = eval(a,b,op) +error
print("{0} {3} {1} ={2}".format(a,b,display_result,op))

ans = input("Y/N ").lower()
if error == 0:
    if ans == "y":
        print("Nice")
    elif ans == "n":
        print("You're wrong")

elif error != 0:
    if ans == "y":
        print("You're wrong")
    elif ans == "n":
        print("Nice")
