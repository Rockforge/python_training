# exercise27.py
class OutOfMoney(Exception):
    pass

try:
    raise OutOfMoney('No money friend :)')
    print(salary)
    int('Ten')
    1/0
except ZeroDivisionError:
    print('You cannot divide by error\n')
except (ValueError, NameError):
    print('Invalid value given\n')
except OutOfMoney:
    print('No money bro')

print('--- End Program ---')
