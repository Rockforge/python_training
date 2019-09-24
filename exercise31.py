# exercise31.py
# Sets
dc = ['Flash', 'Superman', 'Batman', 'Wonder Woman', 'Batman']
marvel = ['Iron Man', 'Hulk', 'Flash', 'Ant-man', 'Ant-man']

dc = set(dc)
marvel = set(marvel)
print(dc)
print(marvel)

print('--- Union ---')
print(dc.union(marvel))
print(dc.intersection(marvel))
print(dc.difference(marvel))
print(marvel.difference(dc))
print(dc.symmetric_difference(marvel))

print('--- Symbols ---')
print(dc | marvel)
print(dc & marvel)
print(dc - marvel)
print(marvel - dc)
print(dc ^ marvel)


print('--- Loop ---')
heroes = dc | marvel
for hero in heroes:
    print(hero)

print('--- Meta data ---')
print(len(heroes))
print(list(heroes))


print('Batman' in heroes)
print('Thanos' not in heroes)