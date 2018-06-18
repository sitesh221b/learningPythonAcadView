#       QUESTION 1

class Circle():
    def __init__(self, radius):
        self.radius = radius

    def getArea(self):
        return 3.14*self.radius**2

    def getCircumference(self):
        return 2*3.14*self.radius


o = Circle(int(input('Enter radius: ')))
print(o.getArea())
print(o.getCircumference())


#       QUESTION 2

class Student():
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

    def Display(self):
        print('Name: '+self.name)
        print('Roll No: '+self.roll)


s1 = Student('Peter', 15)
s1.Display()


#       QUESTION 3

class Temperature():
    def convertCelsius(self, temp):
        return (5/9) * (temp-32)

    def convertFarenheit(self, temp):
        return (temp*(9/5)) + 32


t = Temperature()
print('Temperature in Farenheit: ', t.convertFarenheit(float(input('Enter temperature in Celcius: '))))
print('Temperature in Celcius: ', t.convertCelsius(float(input('Enter temperature in Farenheit: '))))


#       QUESTION 4

class MovieDetails():
    def __init__(self, mName, aName, year, rating):
        self.mName = mName
        self.aName = aName
        self.year = year
        self.rating = rating

    def display(self):
        print('Movie Name: '+self.mName)
        print('Artist Name: '+self.aName)
        print('Year of Release: '+self.year)
        print('Rating: ', self.rating)

    def update(self):
        self.mName = input('Movie Name: ')
        self.aName = input('Artist Name: ')
        self.year = input('Year of Release: ')
        self.rating = input('Rating: ')
        print('Updated!')


m = MovieDetails('Avengers: Infinty War', 'Alan Silvestri', 2018, 8.8)
m.display()
m.update()


#       QUESTION 5

class Expenditure():
    def __init__(self, exp, saving):
        self.exp = exp
        self.saving = saving
        self.sal = 0

    def display(self):
        print('Expenditure: ', self.exp)
        print('Savings: ', self.saving)

    def calculate(self):
        self.sal = self.exp + self.saving

    def dispSal(self):
        print('Salary: ', self.sal)


obj = Expenditure(int(input('Enter expenditures: ')), int(input('Enter savings: ')))
obj.display()
obj.calculate()
obj.dispSal()

