# exercise29.py
# Functions

def greet(name, age = 16):
    print('Hello World')
    print('Hello ' + name)
    print('You are ' + str(age))

def getName():
    return 'Christian'

def getAge():
    return 20

# Positional arguments
greet('Christian Jurilla')
greet('Christian Jurilla', 20)

# Named arguments / Keyword arguments
greet(age=25, name='Christian',)

params = {}
params['name'] = getName()
params['age'] = getAge()

# Access the dict by values
greet(**params)

