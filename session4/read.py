favs = ["Death note","Netflix","Teaching"]

#self - modifying

for index, fav in enumerate(favs):
    favs[index] = fav.lower()

print(favs)

# favs.pop(0)
# print(favs)
