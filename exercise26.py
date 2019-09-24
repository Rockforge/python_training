# exercise26.py
# Dictionary (key-value storage)

record = {
    'name': 'Empoy',
    'movies': [ 'Kita Kita', 'The Barker' ],
    'is pogi': True,
    1024: 'test'
}

record[1024] = 'done'
record[1025] = 'new test'
# del record['name']
print(record)
# print(record['name'])
print(record.get('name', 'Anonymous'))
print(record['is pogi'])

print('--- Iterate by Keys ---')

for key in record:
    print(key)

print('--- Iterate by values ---')

for val in record.values():
    print(val)

print('--- Iterate by items ---')
for key, item in record.items():
    print('{} => {}'.format(key, item))