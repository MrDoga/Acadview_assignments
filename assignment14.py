#Q1.Write a Python program to read last n lines of a file
import os
def Lastline(f,n):
    with open(f) as file:
        print('Last',n,"of file : ",f)
        for line in (file.readline()[-n:]):
            print(line)
name=input("enter file name : ")
n=int(input('number of last lines : '))
try:
    Lastline(name,n)
except:
    print ('error')

#Q2.

file=open("abc","r+")

wordcount={}

for word in file.read().split():
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1

for k,v in wordcount.items():
    print k, v

#Q3.

with open("abc.txt") as f:
    with open("out.txt", "w") as f1:
        for line in f:
            f1.write(line)

#Q4.

with open('abc.txt') as fh1, open('test.txt') as fh2:
    for line1, line2 in zip(fh1, fh2):
        print(line1+line2)

#Q5.
import random
def Rand(start, end, num):
    res = []

    for j in range(num):
        res.append(random.randint(start, end))

    return res
num = 10
start = 20
end = 40
print(Rand(start, end, num))
