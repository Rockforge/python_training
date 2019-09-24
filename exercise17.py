# exercise17.py
# Data type: tuple


denominations = ('pesos', 'centavos')
# denominations = ('pesos',) # this should be the syntax for one element tuples

print(denominations)
print(type(denominations))
print(denominations[1])


print('--- Entering loop ---')
for denomination in denominations:
    print(denomination)

