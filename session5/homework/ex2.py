numbers = [1,6,8,1,2,1,5,6]

num = int(input("Enter a number? "))

count = []

for i,n in enumerate(numbers):
    if num in numbers and num == n:
        count.append(num)

print("{0} appears {1} times in my list".format(num,len(count)))
