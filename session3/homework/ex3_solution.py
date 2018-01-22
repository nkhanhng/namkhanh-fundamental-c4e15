print('''Think of a number from 0 to 100
"c" if my guess is 'C'orrect
"s" if my guess is 'S'maller than your number
"l" if my guess is 'L'arger than your number''')

lo = 0
hi = 100
loop = True
while loop:
    mid = (lo + hi) // 2
    ans = input("Is {0} your number" ).format(mid)
    if ans.lower() == 'c':
        #covert to lowercase
        print("I knew it")
        loop == False
    elif ans.lower() == 's':
        hi = mid
    elif ans.lower() == 'l':
        lo = mid
