import random

word = "champion"
print(' '.join(random.sample(word,len(word))))

ans = input("Enter your answer: ").lower()
if ans == word:
    print("Hura")
else:
    print(":(")
