#Q1. Create a class Animal as a base class and define method animal_attribute.
# Create another class Tiger which is inheriting Animal and access the base class method.

class Animal:
    def animal_attribute(self,loyal,place): #object with animals attribute
        self.loyal = loyal
        self.place = place

class Tiger(Animal):
    def tiger_attribute(self,name,gender,): #tigers attribute
        self.name = name
        self.gender = gender
        self.speechtype = "roar"
        Animal.__intit__(self,'tiger','Ground')

#Q2.

class A:
    def f(self):
        return self.g()

    def g(self):
        return 'A'

class B(A):#A class is inherited in B
    def g(self):
        return 'B'

a = A() #A method is in variable a
b = B() #B method  is in variable b
print a.f(), b.f()
print a.g(), b.g()
# The output of the following programe  will be
# A B
# A B

#Q4.

import math #import math
class Shape:
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.base*self.side*math.sin(math.radians(self.theta))
class Rectangle(Shape):
    def __init__(self,base,side):
        super(Rectangle,self).__init__(base,side)

class Square(Shape):
    def __init__(self, base):
        super(Square, self).__init__(base,base)


#Q3.
class Cop():
    def __init__(self,name,age,work,designation,experience):
        self.name = name
        self.experience = experience
        self.age = age
        self.work = work
        self.designation = designation
    def add(self):
        self.add
    def display(self):
        self.diplay
    def update(self):
        name = input("enter name")
        age = input("enter age")
        work = input("type of work")
        designation = input("designation")
        experience = input("experience")
        print("the",self.name,"is",self.age,"years old and works",self.work,"whos designation is ",self.designation,"and have experience for ",self.experience)



