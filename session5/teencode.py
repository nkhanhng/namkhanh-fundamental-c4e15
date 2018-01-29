dic = {
    "ng": "nguoi-Noi ve con nguoi",
    "ns": "Noi",
    "hc": "hoc",
    "ngta": "Nguoi ta"
}

while True:
    for i in dic:
        print(i,end=' ')

    print()
    print("*" * 10)
    ans = input("Your code: ")

    if ans in dic:
        print(dic[ans])
    else:
        print("Not found")
        add = input("Do you want to contribute this word(Y/N): ")
        if add == "Y":
            trans = input("Enter your tranlation: ")
            dic[ans] = trans
            print("Updated")
        else:
            break
