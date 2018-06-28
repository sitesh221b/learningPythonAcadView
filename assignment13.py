#       QUESTION 1

a = 3
try:
    if a < 4:
        a = a/(a-3)
except ZeroDivisionError:
    print("Don't you know what happens when you divide a number with zero")
else:
    print(a)


#       QUESTION 2

L = [1, 2, 3]
try:
    print(L[3])
except IndexError:
    print('Bhai sambhal ke aage khai hai')


#       QUESTION 3

"""
Output: An exception
Traceback (most recent call last):
    File "<stdin>", line x, in <module>
NameError: Hi there

Reason: since NameError has been raised so it will go to except which explicitly says NameError in which it prints
        "An exception" and then 'raise' will re-raise the error which was caused
"""


#       QUESTION 4

"""
Output: -5.0
        a/b result in 0
"""


#       QUESTION 5

try:
    import nothing
except ImportError:
    print('Ye module nahi hai mere paas')

try:
    x = int(input('Enter a number: '))
except ValueError:
    print('Bhai number ka matlab nahi pata kya?')

s = [1, 2, 3]
try:
    print(s[3])
except IndexError:
    print('Bhai sambhal ke aage khai hai')


#       QUESTION 6

class AgeTooSmallError(Exception):
    print("You're a minor")


def func():
    try:
            age = int(input('Enter Age: '))
            if age < 18:
                raise AgeTooSmallError
    except AgeTooSmallError:
        print('Bhai/Miss Minor hai tu')
        func()
    else:
        print('Congo')


func()
