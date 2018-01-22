favs = ["Death note","Netflix","Teaching"]

for index, fav in enumerate(favs):
    print("{0}. {1}".format(index + 1,fav))

n = int(input("Delete: "))
favs.pop(n-1)

for index, fav in enumerate(favs):
    print("{0}. {1}".format(index + 1,fav))
