def get_even_list(l):
    new_list  = []
    for num in l:
        if num % 2 == 0 :
            new_list.append(num)
    return new_list

even_list = get_even_list([1,4,5,-1,10])
print(even_list)
