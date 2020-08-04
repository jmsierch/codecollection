#! python3
import random

print('This is a coin-flip simulator.')
print('This program will run 1000 times.')

heads = 0

for i in range(1, 1001):
    if random.randint(0, 1) == 1:
        heads = heads + 1
    if i == 500:
        print('Halfway done!')

print('Heads came up ' + str(heads) + ' times.')
