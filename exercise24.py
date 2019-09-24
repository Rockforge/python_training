# exercise24.py

f = open('exercise21.txt', 'r')
print(type(f))
for line in f:
    # print(line.count('\n'))
    print(line, end='')
f.close()