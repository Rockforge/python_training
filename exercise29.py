# exercise29.py
# Functions

def greet(name, age = 16):
    print('Hello World')
    print('Hello ' + name)
    print('You are ' + str(age))

# Positional arguments
greet('Christian Jurilla')
greet('Christian Jurilla', 20)

# Named arguments / Keyword arguments
greet(age=25, name='Christian',)


params = {
    'name': 'Sony Valdez',
    'age': 20
}

# Access the dict by values
greet(**params)