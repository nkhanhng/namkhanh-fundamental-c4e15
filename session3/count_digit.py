num = int(input("Enter a number: "))

count = 1

while True:
    num = num // 10
    if num == 0:
        break
    count += 1
print(count)
