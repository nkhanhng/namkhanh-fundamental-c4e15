st = input("Enter string: ").lower()

letter_counts = {}

for letter in st:
    letter_counts[letter] = letter_counts.get(letter,0) + 1

for key,value in sorted(letter_counts.items()):
    print(key,value)
