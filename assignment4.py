#           QUESTION 1

x = int(input('Enter any year: '))

if(x % 400) == 0:
    print("It's a leap year")
elif(x % 100) == 0:
    print("It's Not a leap year")
elif(x % 4) == 0:
    print("It's a leap year")
else:
    print("It's Not a leap year")


#       QUESTION 2

length = input('Enter Length: ')
breadth = input('Enter Breadth: ')

if length == breadth:
    print('Dimensions are for square')
else:
    print('Dimensions are for Rectangle')


#       QUESTION 3

t = []

for i in range(3):
    t.append(input('Enter age: '))

print('Oldest: ', max(t))
print('Youngest: ', min(t))


#       QUESTION 4

points = int(input('Enter your Points: '))

if points > 200 or points <= 0:
    print('Points Not Valid')
elif 1 <= points < 51:
    print("Sorry! No prize this time.")
elif 51 <= points < 150:
    print("Congratulations! You won a Wooden Dog!")
elif 151 <= points < 180:
    print("Congratulations! You won a Book!")
else:
    print("Congratulations! YOu won a Chocolates")


#       QUESTION 5

q = int(input('Enter Quantity: '))
p = q * 100

if p > 1000:
    disc = .1 * p
else:
    disc = 0

print('Total Cost: ', p - disc)
