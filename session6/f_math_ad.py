from random import *
from calc import eval

a = randint(0,10)
b = randint(0,10)
error = randint(-1,1)

op_list = ["+","-","*","/"]
op = choice(op_list)

display_result = 0
if op == "+":
    display_result = a + b + error
elif op == "-":
    display_result = a - b - error
elif op == "*":
    display_result = a * b * error
elif op == "/":
    if b == 0:
        print("Sorry")
    else:
        display_result = a // b // error
print("{0} {1} {2} ={3}".format(a,op,b,display_result))

ans = input("Y/N ").lower()
if error == 0:
    elif ans == "y":
        print("Nice")
    elif ans == "n":
        print("You're wrong")

elif error != 0:
    if ans == "y":
        print("You're wrong")
    elif ans == "n":
        print("Nice")
