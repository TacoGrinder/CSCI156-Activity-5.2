__author__ = 'Sean'

def divisor(x):
    sum = 0
    for i in range (1, x//2 + 1):

        if x % i == 0:
            print(i)


divisor (12)
