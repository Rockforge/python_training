# exercise29.py
# Functions, Dunder, Main, Docstring

password = '1234'

# Stubbing
def getSecret():
    """
    Get secret
    """
    pass

def greet(name, age = 16):
    print('Hello World')
    print('Hello ' + name)
    print('You are ' + str(age))

def getName():
    return 'Christian'

def getAge():
    return 20

def getHobbies():
    return 'Singing', 'Cooking'

def main():
    # Positional arguments
    greet('Christian Jurilla')
    greet('Christian Jurilla', 20)

    # Named arguments / Keyword arguments
    greet(age=25, name='Christian',)

    params = {}
    params['name'] = getName()
    params['age'] = getAge()
    # Unapacked the return value of this function
    # params['hobby1'], params['hobby2'] = getHobbies()

    # Access the dict by values
    greet(**params)



if __name__ == '__main__':
    main()