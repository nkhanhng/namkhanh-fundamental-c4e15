inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}

# 1
inventory['pocket'] = ['seashell', 'strange berry','lint']
print(inventory)

# 2
inventory["backpack"].remove('dagger')
print(inventory)

# 3
inventory['gold'] += 50
print(inventory)
