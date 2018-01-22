import random

word_list = ["dinosaur","snowflake","caterpillar"]

c = 0 #Correct variable
nc = 0 #incorrect variable

for index,word in enumerate(word_list):
    print(' '.join(random.sample(word_list[index],
        len(word_list[index]))))
    ans = input("Your answer: ").lower()
    if ans == word_list[index]:
        print("Correct")
        c += 1
        print()
        continue
    else:
        print(":(")
        nc += 1
        print()

print("You have {0} correct and {1} incorrect".format(c,nc))
