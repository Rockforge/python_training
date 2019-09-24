# exercise18.py
# unpacking

menu = [
    ('Mann Han', 'Spicy Spareribs', 375),
    ('Mann Han', 'Yang Chow', 140),
    ('Denny\'s', 'Pancake', 200),
    ('Jollibee', 'Spaghetti', 50),
]

template = '{: <10}: {:.<20}{:.2f} pesos'

for restuarant, food, price in menu:
    print(template.format(restuarant, food, price))
