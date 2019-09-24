# exercise8.py

heroes = ['Batman', 'Darna', 'Ironman', 'Kardo Dalisay']
heroes[2] = 'Captian'
heroes.append('Joker')
hero_removed = heroes.pop(3)
# heroes.remove('Kardo dalisay') # Exception occurs here

print(hero_removed)
print('---')

for hero in heroes:
    print('I like ' + hero)
