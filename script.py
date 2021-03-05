import sys
import requests

print(sys.version)
print(sys.executable)


def greet(who_to_greet):
    greeting = 'Hello, this is a script to get the {}'.format(who_to_greet)
    return greeting


print(greet('Gyantech Website Status Code'))

r = requests.get('http://gyantech.in')
print(r.status_code)
print(r.ok)

if r.status_code == 200:
    print('Sarthak Saini')
