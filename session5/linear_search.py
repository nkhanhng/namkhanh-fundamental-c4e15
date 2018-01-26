ls = [7,5,10,8,34,65,12,96]

# solution 1
# num = int(input("Enter a number: "))
# if num in ls:
#     print("Found")
#     found_index = ls.index(num)
#     print("index: ",found_index )
# else:
#     print("Not found")

num = int(input("Enter a number: "))

# Assumption
found_index = -1 #Not_found

# Create a loop to test
for index, n in enumerate(ls):
    if n == num:
        found_index = index
        break

if found_index == -1:
    print("Not fount")
else:
    print("Fount at index",found_index)
