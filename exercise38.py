# exercise38.py
# python debugger

# l - List source 
# l[n] - list line ex. l 12 - See line 12
# c - conintue
# n - next line of code
# p - print ex. p sum
# ! - Execute python command ex. !sum = 'two'
# q - force quit
# s - step into function/method
# up - goes up one stack
# ? - help
# pp - pretty print

def add(a, b):
    c = a + b
    c = 10
    return c

# import pdb; pdb.set_trace() # Creates a breakpoint here. Exception of how noraml python coding convention works
breakpoint() # 3.7
print('Let\'s add 1 + 1')
sum = add(1, 1)
print(sum)