from getpass import getpass
print("Hi there, this is a superuser gateway")
user = "c4e"
pas = "codethechange"

count = 0

while count < 3:
    n = input("Username: ")
    m = getpass("Password: ")

    if n == user:
        if m == pas:
            print("Welcome")
        else:
            print("Wrong Password")
    else:
        if m == pas:
            print("Wrong Username")
        else:
            print("Wrong Username and Password")
    count += 1

    if count == 3:
        print("You have tried 3 times", end=' ')
        print("Your account has been locked")
