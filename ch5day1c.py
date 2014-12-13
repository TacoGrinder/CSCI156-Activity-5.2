__author__ = 'Sean'


def divisor(x):
    y = 0
    for i in range(1, x//2 + 1):

        if x % i == 0:
            y += i
    print(y)
    if x == y:
        print(str(x) + " is Perfect!")
    elif x > y:
        print(str(x) + " is Deficient!")
    elif x < y:
        print(str(x)+ " is Abundant!")

divisor (12)