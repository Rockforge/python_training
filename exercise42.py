# exercise42.py
import csv

data = [
    {
        'id': 1, 
        'name': 'Banana', 
    },
    {
        'id': 2, 
        'name': 'Guava', 
    },
]

with open('exercise42.csv', 'w', newline='') as f:
    field_names = ['id', 'name']
    writer = csv.DictWriter(f, fieldnames=field_names)
    # Write the freaking header my friend
    writer.writeheader()
    for row in data:
        writer.writerow(row)

