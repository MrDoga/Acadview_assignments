Python 2.7.14 (v2.7.14:84471935ed, Sep 16 2017, 20:19:30) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #Q1 creating list
>>> a = ['hi',12345,['hello',6123],{},{'hi': 'oij'},('663','777')]
>>> print(a)
['hi', 12345, ['hello', 6123], {}, {'hi': 'oij'}, ('663', '777')]
>>> #Q2 adding value to list
>>> b = ["google","apple","facebook","tesla","microsoft"]
>>> a.extend(b)
>>> print(a)
['hi', 12345, ['hello', 6123], {}, {'hi': 'oij'}, ('663', '777'), 'google', 'apple', 'facebook', 'tesla', 'microsoft']
>>> #Q3 counting the number of it
>>> print(a.count('tesla'))
1
>>> #Q4 ascending and descending
>>> c = [1,4,5,66,5,7,8,2,5,75,89,45]
>>> c.sort()
>>> print(c)
[1, 2, 4, 5, 5, 5, 7, 8, 45, 66, 75, 89]
>>> c.sort(reverse = 1)
>>> print(c)
[89, 75, 66, 45, 8, 7, 5, 5, 5, 4, 2, 1]
>>> stack = ["luffy","monkey","mugiwara"]
>>> stack.append("nami")
>>> print(stack)
['luffy', 'monkey', 'mugiwara', 'nami']
>>> stack.append("brook")
>>> print(stack)
['luffy', 'monkey', 'mugiwara', 'nami', 'brook']
>>> print(stack.pop())
brook
>>> print(stack.pop())
nami
>>> print(stack)
['luffy', 'monkey', 'mugiwara']
>>> queue = ["car","scooty","tv","mobile"]
>>> print(queue)
['car', 'scooty', 'tv', 'mobile']
>>> queue.append("table")
>>> print(queue)
['car', 'scooty', 'tv', 'mobile', 'table']
>>> queue.append("chair")
>>> print(queue)
['car', 'scooty', 'tv', 'mobile', 'table', 'chair']
>>> print(queue.popleft())

