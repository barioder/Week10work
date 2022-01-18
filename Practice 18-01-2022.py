import random
# Create a pyramid object pattern using multiple numbers


def pyramid():
    n = 5
    x = 0

    while n != 0:
        y = random.randint(0, 9)
        y = str(y)
        print(' ' * n, end='')
        print(y * (x + (1 + (5 - n))), end='')
        print()
        n -= 1
        x += 1


pyramid()

n = 5
x = 0
b = 0
while n != 0:

    # y = random.randint(0, 9)
    # y = str(y)
    print(' ' * n, end='')

    v = x + (1 + (5 - n))
    while v > 0:
        b += 1
        print(b, end='')
        # print(random.randint(1, 9), end='')
        v -= 1



    # print(str(random.randint(1, 9)) * (x + (1 + (5 - n))), end='')
    print()
    n -= 1
    x += 1

