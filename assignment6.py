#Q1. Take 10 integers from user and print it on screen
import end as end

list = [] #empty list
for i in range(10): #create list with 10 element
    list.append(int(input("Enter your desired no. \n")))
    print(list)

#Q2.infinte loop

def text(): #we are defining function of our own
    x = 1
    while x == 1:
        print "abc"

#Q3.

list = []  # empty list
for i in range(5):  # create list with 10 element
    list.append(int(input("Enter your desired no. : ")))
    print(list)
    for num in list: #numbers in old list
        print (num * 2) # square of each number in the old list

#Q4

list = [4,'a',6,7,8,'h,','uip',1.9,1.67,1.8]
list2 = [x for x in list if isinstance(x,int)]#store only int element
list3 = [x for x in list if isinstance(x,str)]#store only str element
list4 = [x for x in list if isinstance(x,float)]#store only float element

print([list],[list2],[list3],[list4] ) #print all the list but seperately ie int list will be stored in int list

#Q5
even = [] # empty list to hold even numbers
odd = [] # empty list to hold odd numbers
for n in range(1, 101):
    if n % 2 == 0:#condition for even
        even.append(n)#adding even numbers
    else:
        odd.append(n)#adding odd number

for n in even:
    print(n)

#Q6

for x in range(4):
    print('*'*x)


#Q7

dict = {'abc' : 16, 'tqe' : 19,'nbm' : 25} #dictionary with name and age
for key in dict.keys():
  print(key,dict[key])











