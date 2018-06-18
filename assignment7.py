#       QUESTION 1


def circle_area(radius):
    return 3.14*radius**2


r = int(input('Enter a radius: '))
print('Area is: ', circle_area(r))


#       QUESTION 2

def perfect(num):
    s = 0
    for i in range(1, num):
        if num % i == 0:
            s += i

    if s == num:
        print('It is a Perfect Number')
    else:
        print('It is NOT a Perfect Number')

    print('Following are the perfect numbers from 1-1000: ')
    i = 1
    while i <= 1000:
        s = 0
        for j in range(1, i):
            if i % j == 0:
                s += j

        if s == i:
            print(i, end=" ")

        i += 1


n = input('Enter a number: ')
perfect(n)


#       QUESTION 3

def table(x):
    if x == 11:
        print('Table Over!')
    else:
        print('12 * ', x, ' = ', 12*x )
        table(x+1)


#       QUESTION 4

p = 1


def power(x, y):
    """
    The function finds x^y using recursion
    :param x: the base
    :param y: the power
    :return: p = the final answer
    """
    global p
    if y == 0:
        return p
    else:
        p *= x
        y -= 1
        return power(x, y)


x = int(input('Enter the base number x: '))
y = int(input('Enter the power y: '))
print('x^y = ', power(x, y))


#       QUESTION 5

def factorial(x):
    global p
    dic = {}
    if x == 1:
        dic[x] = p
        return p
    else:
        p *= x
        return factorial(x-1)


