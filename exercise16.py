# exercise16.py

# Servers and games actually use infinite loop

while True:
    reply = input('Are you cute [y/n]? ')
    if reply == 'n':
        break
    elif reply.lower() != 'y':
        print('That is not a valid input')
        continue

    print('You are cute')


