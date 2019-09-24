# exercise34.py
# Function is a datatype

def greetMorning():
    print('Good morning')

def greetAfternoon():
    print('Good afternoon')

def defaultGreet():
    print('Hello')

# An alternative to switches
functions = {
    '1': greetMorning,
    '2': greetAfternoon,
}

choice = input('1 or 2: ')
greet = function.get(choice, defaultGreet)
greet()