#Q1 creating list

a = ['hi',12345,['hello',6123],{},{'hi': 'oij'},('663','777')] #list with mutiple elements
print(a) #output of list


#Q2 adding value to list

b = ["google","apple","facebook","tesla","microsoft"]#new value that will be added in previous list a
a.extend(b) #extend method is used fro adding element of b into a
print(a) #output


#Q3 counting the number of time an object occurs in a list
print(a.count('tesla'))#this will count the no. of times tesla occur in list a extended with list b


#Q4 creating a list and sorting it in ascending and descending

c = [1,4,5,66,5,7,8,2,5,75,89,45]#list with int data type
c.sort() #sort method which is used to sort the lit in ascending order
print(c) #output
c.sort(reverse = 1) #reverse here is used to sort the list in descending order
print(c) #output


#Q6 implement a stack and queue using lists

stack = ["luffy","monkey","mugiwara"] #stack using list
stack.append("nami") #element that have to be added in stack
print(stack) #output
stack.append("brook") #new element that will be added in stack
print(stack) #output
print(stack.pop()) #remove the last element in stack
print(stack.pop()) #remove the last elemnt in stack
print(stack) #print stack
 #implementing queue using lists
queue = ["car","scooty","tv","mobile"] #queue using list
 print(queue) #output
queue.append("table") #element table is added to the queue
print(queue) #output
queue.append("chair") #element table is added to the queue
print(queue) #output
print(queue.popleft()) #remove the left most element of the queue
print(queue.popleft()) #remove the left most element of the queue
print(queue) #output after removing the 2 names from the left side of the queue

Q
