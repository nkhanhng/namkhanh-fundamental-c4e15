print("Hello, my name is K and these are my sheep size")
sheeps = [5,7,300,90,24,50,75]
print(*sheeps,sep=', ')

total = 0

for j in range(4):
    print("MONTH", j+1,":")
    print("One month has passed, now here is my flock")
    sheeps =[i + 50 for i in sheeps]  #Increase size of sheep
    print(*sheeps,sep=', ')


    biggest = max(sheeps) #Find biggest sheep to shear
    total += biggest

    print("Now my biggest sheep has size", biggest,"Let's shear it")
    df = sheeps.index(biggest)
    sheeps.remove(biggest)
    sheeps.insert(df,8)

    print("After shearing, here is my flock")
    print(*sheeps, sep=', ')

    print()

print("My flock has size in {0}".format(total))

money = 0
money = total * 2

print("I would get {0} * 2$ = {1}".format(total,money))
