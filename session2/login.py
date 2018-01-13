from getpass import getpass
user = "c4e"
pas = "codethechange"

n = input("Username: ")
m = getpass("Password: ")

if n == user:
    if m == pas:
        print("Welcome")
    else:
        print("Wrong Password")
else:
    print("User not valid")
