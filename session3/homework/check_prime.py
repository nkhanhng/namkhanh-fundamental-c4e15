num = int(input("Enter a number: "))


while True:
    if num < 2:
        print("Khong phai so nguyen to")
    for i in range(2,num + 1):
        if num == 2:
            print("So nguyen to")
        elif num % i == 0:
            print("Khong phai so nguyen to")
        else:
            print("So nguyen to")
        break
    break
