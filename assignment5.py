#Q1. Take input from user and check whether it is leap year or not

year = input("enter your desired year: ") #user will input year
if(year%4==0): #leap year come every 4 year
    print("it is leap year")
else:
    print("year is not leap year")


#Q3. age of three people determine who is oldest and youngest

a = input("enter age of first person:")
b = input("enter age of second person")
c = input("enter age of third person")
if (a > b & a > c): #if a is greater then b and c
    print("a is older then b and c")
    if(b>c & b>a):#if b is greater then a and c
        print("b is older then a and c ")
        if(c>a & c>b):#if c is greater then b and a
            print("c is older then a and b")
        else:
            print("c is younger then a and b")
    else:
        print("b is younger then a and c")
else:
    print("a is younger then b and c")

#Q2Take length and breadth input from the user and check whether  the dimensons  are of square or rectangle

a = input("enter length") #inputs length
b = input("enter breadth")#inputs breadth
if(a==b): #is both sides are equal then print square
    print("its a square")
else: #if both sides are not equal then its a rectangle
    print("its a rectangle")

#Q4
p = input("input the required point for the team : ") #input given by user p signify points

if (p <= 50): #if point is lower then 50
    print("sorry no prize")

elif (p <= 150):# if point is between 51 - 150
    print("Congratulations! you won  a wooden dog ")

elif (p <= 180):# if point is between 151 - 180
    print("Congratulations! you won  a book ")

elif (p <= 200):# if point is between 181 - 200
    print("Congratulations! you won  a chocolate")




