#Q1. What is tuple?
#date and time module supplies classes for manipulating dates and times in both simple and complex ways.
#time() is used to count the no. of seconds
#gmtime() is used to return a structure with 9 values each representing a time attribute(days,years,months etc) in sequnce


#Q2.Write a program to get formatted time.
import time
print time.ctime() #ctime is used to show the current time along with date,month and year

#Q3.  Extract month from the time.

import datetime
d = datetime.date.today()
print (d.month) #print only month

#Q4. Extract day from the time.

import datetime
d = datetime.date.today()
print (d.day) #print only day

#Q6 Write a program to print time using localtime method.

import time
print time.localtime()

#Q7 Find the factorial of a number input by user using math package functions.

n = (int(input("enter your no."))) #user will input his/her desired number
import math
print math.factorial(n)

#Q8 Find the GCD of a number input by user using math package functions.

import math
m = (int(input("enter desired no.")))
print math.gcd(m) #gcd is greatest common divisor

#Q9 Use OS package and do the following tasks:
#1. Get current working directory.
#2. Get the user environment.

import os
print os.getcwd() #get the current working directory
print os.environ



