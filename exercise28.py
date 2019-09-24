# exercise28.py
# Random

import random # Using this library

heroes = ['Batman', 'Kardo Dalisay', 'Thanos', 'Thor', 'Saitama']

best = random.choice(heroes)
power = random.randint(9000, 10000)

template = 'The best hero is {}. Their power level is {}'
output = template.format(best, power)

print(output)

if power > 9000:
    print('Their power level is over 9000!!!')



cards = ['❤', '🍀', '♠', '♦']
print(cards)
print(random.choice(cards))




