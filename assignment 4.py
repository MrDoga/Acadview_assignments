#Q1. WAP to create a tuple with different data types and find its length
tuple = () #empty tuple
print(tuple)#output

tuple = (1,2,3) #tuple have int data type
print(tuple)#output

tuple1 = (1,"good morning",5.5 , "hello") #tuple with different data types
print(tuple1)

len(tuple1) #it will find the length of the tuple
print(len(tuple1)) #this will print the length of the tuple

#if we want to find the length of the multiple tuple then 

print "length of first tuple : " , len(tuple)
print "length of second tuple : " , len(tuple1)

#Q2. finding the largest and smallest elements of a tuples

#for this we will take tuple1
print "largest element in tuple is : " , max(tuple1) #max method will print the largest of element in tuple2
print "smallest element in tuple is : " , min(tuple1) #it will print smallest element in a tuple
#the smallest and largest elements are chosen according to their ascii code

#Q3 multiplying elements of a tuple

tuple2 = (1,3,4)#new tuple
print ("new tuple is :" + str(tuple2))#out of new tuple
tuple2 = (1*3*4)
print ("product of new tuple is :" + str(tuple2))#it will give product of tuple2

#Q4creating 2 sets of user defined values
#1.calculate diff between 2 sets
#2.compare 2 sets
#3print sresult of intersection of 2 sets

A= {1,2,3,4} #set of elements
B = {2,3,5}
print (A,B) #output

#now we have to calcualte difference between 2 sets (set1 and set2)
print(B - A)#elements that exist only in set B but not in set A
print(A - B)#elements that exist only in set A but not in set B

#for intersection of 2 sets we will assume the above 2 sets A and B
print (A & B)


#Q Create a dictionary to store name and marks of 10 students by user input
dictionary = {}
count = 0 #initial count will be 0
while count < 10: #start of loop, it will stop when it gets 10 input
    name = raw_input("Enter yout name:")#raw_input gets input from the user and returns the data as a string
    mark = input("enter your marks:")
    if name not in dictionary:
        dictionary[name] = mark #if name is not in dictionary it will be mark
        count = count + 1#increment
print dictionary #output
