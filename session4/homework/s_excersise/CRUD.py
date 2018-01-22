items = ['T-Shirt','Sweater']

def out():
    print("Our items: ",end=' ')
    print(*items,sep=', ')


while True:
    ans = input("Welcome to our shop, what do you want(C,R,U,D)(E to exit) ").upper()

    #Read
    if ans == "R":
        out()

    #Create
    elif ans == "C":
        add = input("Enter new item: ")
        items.append(add)
        out()

    #Update
    elif ans == "U":
        up = int(input("Update position: "))
        if up > len(items):
            print("Not in list")
        else:
            add = input("New item: ")
            items[up - 1] = add
            out()

    #Delete
    elif ans == "D":
        rm = int(input("Delete position: "))
        if rm > len(items):
            print("Not in list")
        else:
            items.pop(rm - 1)
            out()

    elif ans == "E":
        break
