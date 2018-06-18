#       QUESTION 1


class Animal:

    def animal_attribute(self):
        print('This is base class')


class Tiger(Animal):
    def tiger_func(self):
        print('This is derived class')


obj = Tiger()
obj.animal_attribute()


#       QUESTION 2

class A:
    def f(self):
        return self.g()

    def g(self):
        return 'A'


class B(A):
    def g(self):
        return 'B'


a = A()
b = B()

print(a.f(), b.f())
print(a.g(), b.g())

"""
    Output: A B
            A B
    
    a.f() => will call the function f() of class A which returns self.g() that means it will call g() function of the 
             same object hence that will return character 'A'
    
    b.f() => will call the function f() from class A as it's inherited in B and again it'll reach function g() but this 
             time B's as B's object is used
    
    a.g() => will directly call the g() function class A and returns 'A'
    
    b.g() => will directly call g() and returns 'B'                   
    
"""


#       QUESTION 3

class Cop:
    def __init__(self, name, age, work, exp, desg):
        self.name = name
        self.age = age
        self.work = work
        self.exp = exp
        self.desg = desg

    def add(self):
        self.name = input('Enter Name: ')
        self.age = input('Enter Age: ')
        self.work = input('Enter Work: ')
        self.exp = input('Enter Experience: ')
        self.desg = input('Enter Designation: ')

    def display(self):
        print('Name: ', self.name)
        print('Age: ', self.age)
        print('Work: ', self.work)
        print('Experience: ', self.exp)
        print('Designation: ', self.desg)

    def update(self):
        self.name = input('Update Name: ')
        self.age = input('Update Age: ')
        self.work = input('Update Work: ')
        self.exp = input('Update Experience: ')
        self.desg = input('Update Designation: ')


class Mission(Cop):
    def __init__(self):
        self.mission = ""

    def add_mission_details(self):
        self.mission = input('Give mission details: ')


obj = Mission()
obj.add()
obj.display()
obj.update()


#       QUESTION 4

class Shape:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth


class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth


class Square(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth


r = Rectangle(input('Enter Length: '), input('Enter Breadth'))
print('Area of Rectangle: ', r.area())

s = Square(input('Enter Length: '), input('Enter Breadth: '))
print('Area of Square: ', s.area())


