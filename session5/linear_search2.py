nums = [7,5,10,8,34,65,12,96]

num_to_find = int(input("Enter a number: "))

for index,num in enumerate(nums):
    if num == num_to_find:
        print("Found at index: ",index)
        break
else:
    print("Not found")
