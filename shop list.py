shop_list = []
item = None
description = None

print('Please enter the items of the shopping list (type: quit to finish):')

while item != 'quit':
    item = input('Item: ')
    if item != 'quit':
        shop_list.append(item)

while description != 'stop':
    description = input('Description of item: ')
    if description != 'stop':
        shop_list.append(description)

         
print()

print('the shopping list is:')
for item in shop_list, description in shop_list:
    print(f'{item}" - "{description}')

print()
print('The shopping list with indexes is: ')
for i in range(len(shop_list)):
    item = shop_list[i]
    print(f'{i}. {item}')

index = int(input('Which item would you like to change? '))
new_item = input('What is the new item? ')

shop_list[index] = new_item

print("\nThe shopping list with indexes is:")
for i in range(len(shop_list)):
    item = shop_list[i]
    print(f"{i}. {item}")

