#python

#count vowels in a string

string="aishu"
vowels='a','e','i','o','u'
count=0
for x in string:
    if x in vowels:
        count+=1
print(count)


#find second largest number in list

list1=[3,7,2,9,1]
large=float('-inf')
second=float('-inf')
for x in list1:
    if x>large:
        second=large
        large=x
    elif x >second and x!=large:
        second=x
print(second)


#reverse a string without using slicing

string="hello"
s=""
for i in range(len(string)-1,-1,-1):
    s+=string[i]
print(s)





















