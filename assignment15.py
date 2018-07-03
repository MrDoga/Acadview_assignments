#Q1. Extract the user id, domain name and suffix from the following email addresses.
#emails = "zuck26@facebook.com" "page33@google.com"
"jeff42@amazon.com"

import re
result1 = re.split(r'[.@]+','zuck26@facebook.com') #here we used character class
result2 = re.split(r'[.@]+','page33@google.com')
result3 = re.split(r'[.@]+','jeff42@amazon.com')
desired_output = (result1,result2,result3)
print desired_output

#Q2 Retrieve all the words starting with ‘b’ or ‘B’ from the following text

import re
value = "Betty bought a bit of butter, But the butter was so bitter, So she bought some better butter, To make the bitter butter better.t" #input
a = re.findall("[bB]\w+", value)#find all words starting with B and b
print(a)


#Q3.

rmv = ".,;_"
s = "A, very very; irregular_sentence"
for c in rmv:
    s=s.replace(c,'')
    s.split()
