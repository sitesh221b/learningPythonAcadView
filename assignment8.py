#       QUESTION 2

import time
import math
import os

print('Formatted Time: ', time.asctime())


#       QUESTION 3

print('Month: ', time.gmtime().tm_mon)


#       QUESTION 4

print('Day: ', time.gmtime().tm_mday)


#       QUESTION 5

print('Date: ', time.gmtime().tm_mday)


#       QUESTION 6

print('Time: ', time.localtime().tm_hour, ':', time.localtime().tm_min, ':', time.localtime().tm_sec)


#       QUESTION 7

print('Factorial: ', math.factorial(int(input('Enter a number: '))))


#       QUESTION 8

print('GCD: ', math.gcd(int(input('Enter 1st number: ')), int(input('Enter 2nd number: '))))


#       QUESTION 9

print('My current working directory: ', os.getcwd())
print('Environment: ', os.environ())
