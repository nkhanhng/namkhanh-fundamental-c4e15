p = []

for i in range(5):
    if i == 0:
        p.append(1)
    elif i == 1:
        p.append(2)
    else:
        p.append(p[i-1] + p[i-2])
    print("Month {0}: {1} pair(s) of rabbits".format(i,p[i]))
