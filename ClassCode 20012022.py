# create a tuple, using the while loop to print out all the items

cars = ('BMW', 'Benz', 'Jeep', 'Ford')

i = 0
while i < len(cars):
    print(cars[i])
    i += 1

print('-------------------------------------------------')
# using list comprehenssion print out odd numbers only

oddNum = [a for a in range(1, 15, 1) if a % 2 == 1]

for num in oddNum:
    print(num)

print('-------------------------------------------------')

# create a nesting list that prints 1 list all in upper case and second list in lower case

cars = ['BMW', 'Benz', 'Jeep', 'Ford']
colors = ['Blue', 'Red', 'Yellow', 'Green']

for car in cars:
    for color in colors:
        print(f'{color.lower()} {car.upper()}')

print('-------------------------------------------------')

# Create a if, elif, else statement using the user input that
# prints "This is a odd number" while it is odd and prints this is even
# if it is an even number in the range of 10 and last satement is done

while True:
    v = input('Do you want a list of odd and even numbers?(y/n) ').lower()
    if v == 'y':
        for i in range(1, 10):
            if i % 2 == 0:
                print(f'{i} is an even number')
            elif i % 2 == 1:
                print(f'{i} is an odd number')
            else:
                print('failed')
    else:
        print('DONE')
        break

print('-------------------------------------------------')

# Create 2 list and combine it to 1 then print all the items using the for lop

cars = ['BMW', 'Benz', 'Jeep', 'Ford']
colors = ['Blue', 'Red', 'Yellow', 'Green']

comb = cars + colors

for item in comb:
    print(item)