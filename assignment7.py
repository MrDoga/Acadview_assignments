#Q1 Create a function to calculate the area of a circle by taking radius from user.
n = int(input("enter the radius :"))
pi = 3.146578
def radius(r):
    a = pi*n**2
    return(a)
print radius(n)


#Q2. Use function in a program that determines and prints all the perfect numbers between 1 and 1000.

n = int(input("Enter any number: ")) #user will input
sum = 0
for i in range(1, n):
    if(n % i == 0):
        sum = sum + i
if (sum == n):
    print("The number is a Perfect number!")
else:
    print("The number is not a Perfect number!")


#Q3.  Print multiplication table of 12 using recursion.

def timetable(n, t=1):
    if t <= 10:
        print(str(n) + "x" + str(t) + "=" + str(n*t))
        timetable(n, t+1)
    else:
        return
timetable(12)

#Q4  Write a function to calculate power of a number raised to other ( a^b ) using recursion.

def power(a,b):
    if(b==1):
        return a
    else:
        return a*power(a,b-1)#it will return a^b
print power(2,3) #result will be 2*2*2

#Q5

list = []
def factorial(n):
    if(n <= 1):
        return 1
    else:
        return(n*factorial(n-1))
n = int(input("Enter number:"))
print("Factorial:")
print factorial(n)
dict={n:factorial(n)}
print(dict)




