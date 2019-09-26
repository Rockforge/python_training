# exercise40.py
import csv

data = [
    [1, 'Banana', ],
    [2, 'Guava', ],
    [3, 'Apple', ],
    [4, 'Straw|Berry', ],
]

# Context manager
with open('exercise40.csv', 'w', newline='') as f:
    writer = csv.writer(f, delimiter='|', quotechar='\'')
    for row in data:
        writer.writerow(row)

