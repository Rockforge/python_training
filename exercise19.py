# exercise19.py
# enumerate

menu = [
    ('Mann Han', 'Spicy Spareribs', 375),
    ('Mann Han', 'Yang Chow', 140),
    ('Denny\'s', 'Pancake', 200),
    ('Jollibee', 'Spaghetti', 50),
]

for index, row in enumerate(menu, 1):
    print('{}: {}'.format(index, row))