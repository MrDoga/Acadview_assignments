#Q1. Name and handle the exception occured in the following program:
 #a=3
 #if a<4:
    #a=a/(a-3)
     #print(a)

#the exception occured in following program is ZeroDivisionError which occur while diving an variable with zero
#program to handle the exception will be
try:
    a = 3
    if a<4:
        b = a/(a-3)
    print("value is :" , b)

except(ZeroDivisionError,NameError):
    print("error handled")

#Q2. Name and handle the exception occurred in the following program:
#l=[1,2,3]
#print(l[3])

#exception  occured in the above program will be IndexError
b = [1,2,3]
try:
    print("2nd element = %d" %(a[1]))
    print("4th element = %d" %(a[3]))
except IndexError:
    print("error is handled")

#Q3. What will be the output of the following code:
#try:
    #raise NameError("Hi there")
#except NameError:
    #print "An exception"
    #raise

#An exception
# NameError: Hi there
# will be the output of this code. An exception will be definitely print no matter what.

#Q4.What will be the output of the following code:
#def AbyB(a , b):
#	try:
#		c = ((a+b) / (a-b))
#	except ZeroDivisionError:
#		print "a/b result in 0"
#	else:
#		print c

#AbyB(2.0, 3.0)
#AbyB(3.0, 3.0)


#the output of the following program will be
#-5.0
#a/b result in 0
#everytime if there is a ZeroDivisionError it will print a/b result in 0
#AbyB(2.0,3.0) and AbyB(3.0,3.0) are use to test following program a and b are taken as (2.0 ,3.0) and (3.0,3.0) seperately
#thats why on executing 3.0 and 3.0 the program is printing a/b result is 0


#Q5.Write a program to show and handle following exceptions:
#1. Import Error
#2. Value Error
#3. Index Error

#for import error
try:
    from __cowtown import *
except ImportError:
    raise ImportError("error")

#for value error

a="hello"
try:
    print(int(a))
except Exception as e:
    print("exception is handled")

#for index error

l=[1,2,3]
try:
    print("3rd element",l[3])
except Exception as e:
    print("exception is handled")

#Q6.Create a user-defined exception AgeTooSmallError() that warns the user when they have entered age less than 18.
# The code must keep taking input till the user enters the appropriate age number(less than 18).

class Error(Exception):
    pass
class AgeTooSmallError(Error):
    pass
while True:
    try:
        age=input("enter age:")
        if age<18:
            raise AgeTooSmallError

    except AgeTooSmallError:
        print("entered age is wrong")
    else:
        print("age is correct")
