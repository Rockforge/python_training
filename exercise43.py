# exercise43.py
import csv

with open('exercise42.csv', 'r', newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row.items())

