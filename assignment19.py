#Q1 Create a numpy array with 10 elements of the shape(10,1) using np.random and find out the mean of the elements using basic numpy functions.

import numpy
x = numpy.random.rand(10,1)
b = numpy.mean(x)#numpy function to find mean
print x
print "mean of the above random numbers is : ",b

#Q2.Create a numpy array with 20 elements of the shape(20,1) using np.random find the variance and standard deviation of the elements.
import numpy
a = numpy.random.rand(20,1)
c = numpy.std(a)
d = numpy.var(a)
print a
print"standard deviation of above elements is : ",c
print"variance of above elements is : ",d

#Q3.

import numpy
y = numpy.random.rand(10,20)
print "array of A is : ",y
g = numpy.random.rand(20,25)
print "array of B is : ",g
k = numpy.matmul(y.g)
print k
l = x.sum(k)
