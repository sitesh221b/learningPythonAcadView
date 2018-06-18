#       QUESTION 1

x = [input('Enter a value: ') for i in range(10)]

for i in x:
    print(i)


#       QUESTION 2

# while True:
#     print("Dormammu! I've come to bargain.")


#       QUESTION 3

size = input('Enter size of list: ')
List1 = [int(input('Enter a value')) for i in range(int(size))]
List2 = []

for i in List1:
    List2.append(i*i)

print(List2)


#       QUESTION 4

mixList = [1, 6, 14000605, 'Tony', 'Steve', 'Thanos', .00000714254]
intList = []
floatList = []
strList = []

for i in mixList:
    if type(i) == int:
        intList.append(i)
    elif type(i) == float:
        floatList.append(i)
    else:
        strList.append(i)


#       QUESTION 5

evenList = []
oddList = []

for i in range(1, 101):
    if i % 2 == 0:
        evenList.append(i)
    else:
        oddList.append(i)


#       QUESTION 6

for i in range(4):
    for j in range(i+1):
        print('*', end='')
    print()


#       QUESTION 7

D = {'name': 'Peter Parker', 'madeup-name': 'Spider-Man'}
for i in D:
    print(i + ' => ' + D[i])


#       QUESTION 8

size = input('Enter size of the list: ')
L = [input('Enter an integer: ') for i in range(int(size))]
x = input('Enter the integer to search: ')

i = 0

for i in L:
    if x == i:
        L.remove(i)
    else:
        print('Element not found!')

