import random
# create a function to find
n = 5
evenNumbers = []
notEven = []
def ave(n):
    while n > 0:
        randomNum = random.randint(1, 14)
        if randomNum % 2 == 0:
            evenNumbers.append(randomNum)
        else:
            notEven.append(randomNum)

            continue

        n -= 1

    print(evenNumbers)

    evenTuple = tuple(evenNumbers)
    print(evenTuple)

    average = sum(evenTuple)/len(evenTuple)

    return f'{round(average,1)} is the average of the tuple'

print(ave(5))

print(notEven)

print('---------------------------------------------')
# create a tuple and you going to convert into a list and pop an element out
tupItems = (1, 2, 3, 4, 5)

listItems = list(tupItems)
print(listItems)
listItems.pop(1)

print(listItems)

print('---------------------------------------------')


# create a nexting tuple and print out all the elements

tuple = ('Num', (1, 2, 3), "Let", ('A', 'B', 'C'))
for item in tuple:
    print(item)

