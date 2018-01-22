print("Hi there, here you favorite things so far")

things = ["death note","netflix","teaching"]
print(things, sep=', ') #pythonic
print("*" *10)

# print(*enumerate(things))
# position = 1
# for i in things:
#     print("{0}. {1}".format(position, i))
#     position += 1

for index, fav in enumerate(things):
    print("{0}. {1}".format(index + 1, fav))
