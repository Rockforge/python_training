# exercise25.py

restaurants = ('Mann Han', 'Mann Han', 'Denny\'s', 'Jolibee')
foods = ('Spicy Spareribs', 'Yang Chow', 'Pancake', 'Spaghetti')
prices = (375, 140, 200, 50)

menu = zip(restaurants, foods, prices)
print(list(menu))


for restaurant, food, price in zip(restaurants, foods, prices):
    print(restaurant, food, price)