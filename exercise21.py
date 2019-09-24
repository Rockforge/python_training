# exercise21.py

# From this
# f = open('exercise21.txt', 'w')
# f.write('Hello World')
# f.close()

# To this
# Context manager
with open('exercise21.txt', 'w') as f:
    f.write('Hello World')