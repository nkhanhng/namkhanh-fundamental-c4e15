b = int(input("How many B bacterias are there? "))

time = int(input("How much time in minutes will we wait? "))

for i in range(2,time+1):
    if i % 2 == 0:
        b *= 2

print("After {0} minutes, we would have {1} bacterias".format(time,b))
