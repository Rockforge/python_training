# exercise41.py
import csv

data = [
    [1, 'Banana', ],
    [2, 'Guava', ],
    [3, 'Apple', ],
    [4, 'Straw|Berry', ],
]

# Context manager
with open('exercise40.csv', 'r', newline='') as f:
    reader = csv.reader(f, delimiter='|', quotechar='\'')
    for row in reader:
        print(row)
        # writer.writerow(row)

