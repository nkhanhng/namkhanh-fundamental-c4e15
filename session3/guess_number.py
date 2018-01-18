from random import randint

x = randint(1, 100)
loop = True
count = 1
while loop:
    num = int(input("The number is "))
    if num < x:
        print("Too small")
    elif num > x:
        print("Too large")
    else:
        print("Bingo")
        loop = False
    count += 1
