count = 0
while count < 5: #True
    yob = int(input("Your year of birth? "))

    age = 2018 - yob

    if age < 10:
        print("Baby")
    elif age < 18:
        print("Teenager")
    else:
        print("Adult")

    count += 1
    # if count >= 5:
    #     break
