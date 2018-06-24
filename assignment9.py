#Q1. Create a circle class and initialize it with radius. Make two methods getArea and getCircumference inside this class.

class Circle():
    def __init__(self,r): #initialize of radius class
        self.radius = r
    def getArea(self): #initialize of get area
        return 3.14*self.radius*self.radius # logic/formulae of area
    def getCircumference(self):#initialize of circumference
        return self.radius*2*3.14

#Q2. Create a student class and initialize it with name and roll number.Make method to display the information
class Student():
    def __init__(self,name,roll):
        self.name = name
        self.roll = roll
    def display(self): #used for displaying
        print self.name #print name
        print self.roll #print roll number

#Q3. Create a Temprature class. Make two methods :
# 1. convertFahrenheit - It will take celsius and will print it into Fahrenheit.
# 2. convertCelsius - It will take Fahrenheit and will convert it into Celsius.

class Temprature():
  def  convertFahrenhiet(self,celsius):
    return (celsius*(9/5))+32
  def convertCelsius(self,farenhiet):
    return (farenhiet-32)*(5/9)

#Q4  Create a class MovieDetails and initialize it with Movie name, artistname,Year of release and ratings
#Make methods to
#1. Display-Display the details.
#2. Update- Update the movie details.

class MovieDetails():
    def _init_(self):
        self.MovieName = ("deadpool2")
        self.ArtistName = ("nma")
        self.Year = 2018
        self.Rating = 5
    def display(self):
        print self.MovieName
        print self.ArtistName
        print self.Year
        print self.Rating

#Q5 Create a class Expenditure and initialize it with expenditure,savings.Make the following methods
#1. Display expenditure and savings
#2. Calculate total salary
#3. Display salary

class Expenditure():
    def __init__(self):
        self.Expenditure = 5000
        self.Savings = 1500

    def display(self):
        print self.Expenditure
        print self.Savings

    def __add__(self):
        self.Salary = self.Expenditure + self.Savings
    def display(self):
        print self.Salary





