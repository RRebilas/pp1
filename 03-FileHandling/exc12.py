product = input('Enter another product to buy: ')
with open('./shoppinglist.txt', 'a+') as file:
    file.write(f'{product}\n',)