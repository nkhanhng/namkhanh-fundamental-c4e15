num = int(input("Enter a number: "))

if num < 2:
    print("{0} is not a prime number".format(num))
for i in range(2,num + 1):
    if num == 2:
        print("{0} is a prime number".format(num))
    elif num % i == 0:
        print("{0} is not a prime number".format(num))
    else:
        print("{0} is a prime number".format(num))
    break
