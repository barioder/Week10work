x, y, z = 1, 2, 3
z, x, y = x, y, z

print(x, y, z)

vowels = ('a', 'e', 'i', 'o', 'u')
#
print(vowels.index('e'))

# indexing tuples
print(vowels[1])

print(vowels.count('a'))


vowels = ('a', 'e', 'i', 'o', 'u', 'i', 'e')

print(vowels.count('e'))

print(vowels.count('a'))
for i in vowels:
    print(i)
if 'a' in vowels:
    print("True")

else:
    print('False')

tup = ('car', 'bike', 'boat')

a, b, c = tup

print(a, c, b)

# number of elements in tuple

print(len(tup))

i = 0

while i != len(tup):
    if 'car' in tup:
        print("yes")
        i += 1
    else:
        break


inPut = input("Enter a vowel ").lower()

if inPut in vowels:
    print('yes it is ')
else:
    print('You wish')


tupG = 25, 56, 26, 10


def sumofvalues(tuptosum):
    s = sum(tuptosum)
    return str(s)

print(sumofvalues(tupG))