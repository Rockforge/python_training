# exercise45.py
import os, pprint

print(os.environ.get('password', '<default>'))
 
pprint.pprint(dict(os.environ))