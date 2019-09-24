# exercise4.py


age = int(input('How old are you? '))


if age >= 150 or age <= 0:
    print('That is not a valid age')
elif age >= 18:
    print('You can dirve')
else:
    print('You cannot drive')
    print('Wait a few more years')