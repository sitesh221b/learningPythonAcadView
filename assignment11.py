import threading
import time

#		QUESTION 1

def func():
	print(threading.currentThread().getName(),'Thread starts')
	time.sleep(5)
	print('Did you miss me?')
	
t = threading.Thread(name="func", target=func)
t.start()


#		QUESTION 2

def numbers():
	for i in range(1, 11):
		print(threading.currentThread().getName(), i)
		time.sleep(1)

q = threading.Thread(name="Numbers: ", target=numbers)
q.start()


#		QUESTION 3

def Print():
	L = [1, 2, 3, 4, 5, 6]
	delay = 2
	for i in L:
		print(threading.currentThread().getName(), i)
		time.sleep(delay)
		delay += 2

t = threading.Thread(name="List Items: ", target=Print)
t.start()


#		QUESTION 4

def fact(n):
	f = 1
	for i in range(n, 0, -1):
		f *= i
	print(threading.currentThread().getName(), f)

n = int(input("Enter a number: "))
t = threading.Thread(name="Factorial: ", target=fact, args=(n,))
t.start()