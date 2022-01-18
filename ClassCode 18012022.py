import random

# create a python game using conditional statements.(User input)

while True:
    userInput = int(input('please enter any number between 1 - 10: '))
    randomInt = random.randint(1, 10)
    # print(randomInt)
    if userInput == randomInt:
        print('!!!!!You Won!!!!!!!')

    elif userInput not in range(1, 11, 1):
        print('!!!ONLY NUMBERS BETWEEN 1 - 10!!!')
        continue

    elif userInput > randomInt:
        if (userInput - randomInt) < 3:
            print('That was close !!!')
        else:
            print('That was not even close!!')
    elif userInput < randomInt:
        if (randomInt - userInput) < 3:
            print('That was close!!!')
        else:
            print("That was not even close")

    else:
        print('Out of Service')

    again = input('Try again? (n/y) ').lower()
    if again == 'y':
        continue
    else:
        print('Thank you for playing with us.\n')
        break


# Create a pyramid object pattern using multiple numbers
n = 5
x = 0

while n != 0:
    # y = random.randint(0, 9)
    # y = str(y)
    print(' ' * n, end='')

    v = x + (1 + (5 - n))
    while v > 0:
        print(random.randint(1, 9), end='')
        v -= 1



    # print(str(random.randint(1, 9)) * (x + (1 + (5 - n))), end='')
    print()
    n -= 1
    x += 1
