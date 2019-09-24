# quiz5.py
# Make a program that shows a menu for a restaurant
# Ask the user what they want to order
# Print the receipt

# Menu list that contains tuples
menu = [
    ('Mann Han', 'Spicy Spareribs', 375),
    ('Mann Han', 'Yang Chow', 140),
    ('Denny\'s', 'Pancake', 200),
    ('Jollibee', 'Spaghetti', 50),
]

total = 0
file_name = 'order.txt'

with open(file_name, 'w') as f:
    f.write('--- RECEIPT ---\n')

while True: 
    for index, row in enumerate(menu, 1):
        restaurant, food, price = row
        print('{}. {: >10}: {:.<20}{:.2f}'.format(index, restaurant, food, price))

    order = int(input('Select an order: ')) # Try-except

    if order > len(menu) or order <= 0:
        print('Order does not exist')
        continue

    total = total + menu[order-1][2] # Get the price

    with open(file_name, 'a') as f:
        f.write('{: >10}:{}{}\n'.format('Restaurant', '.' * 10, menu[order-1][0]))
        f.write('{: >10}:{}{}\n'.format('Food', '.' * 10, menu[order-1][1]))
        f.write('{: >10}:{}{} Pesos\n'.format('Price', '.' * 10, menu[order-1][2]))
    
    decide = input('Wanna order again[Y/N]: ')

    if decide.lower() == 'n':
        with open(file_name, 'a') as f:
            f.write('---TOTAL: {} Pesos'.format(total))
        break
    elif decide.lower() == 'y': 
        continue
    else:
        print('Invalid input')
        continue


print('Receipt is saved at {}. Have a nice day!'.format(file_name))
