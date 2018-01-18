from random import randint

print('''Think of a number from 0 to 100
"c" if my guess is 'C'orrect
"s" if my guess is 'S'maller than your number
"l" if my guess is 'L'arger than your number''')


x = randint(1, 100)
loop = True
count = 0
while loop:
    print("Is", x," your number", end=' ')
    ans = input()
    count += 1
    if ans == "c":
        print("I knew it")
        loop = False
    elif ans == "s":
        x = randint(x,100)
    elif ans == "l":
        x = randint(1,x)
