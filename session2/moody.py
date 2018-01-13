from random import randint

x = randint(0,100)
print(x)
if x < 30:
    print("So sad")
elif 30 <= x < 60:
    print("OK")
else:
    print("Happy")
