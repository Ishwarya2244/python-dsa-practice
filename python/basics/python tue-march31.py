##👉 A function is:
##➡️ a reusable block of code
##
##| Type    | Output      |
##| ------- | ----------- |
##| print() | shows       |
##| return  | gives value |
##
##
##🧠 SIMPLE UNDERSTANDING
##
##👉 def → define function
##👉 () → input place
##👉 call function → run it
##
##🟢 Q1
##
##👉 Create function to print your name

def name():
    print("Aishu")
name()


#2.Function to add two numbers

def add(a,b):
    return a+b
print(add(8,7))


#3.Function to check even or odd

def check(num):
    if num % 2==0:
        return "Even"
    else:
        return "Odd"
print(check(7))



#4.Function to find maximum of 3 numbers
##
def num(list1):
    maxi=list1[0]
    for x in list1:
        if x>maxi:
           maxi=x
    return maxi
print(num([3,7,2]))

        

#5.Function to count vowels in a string

def strings(name):
    vowels='a','e','i','o','u'
    count=0
    for x in name:
        if x in vowels:
            count+=1
    return count
print(strings("aishu"))
    

#6.Function to reverse a string

def string1(name):
    return name[::-1]
print(string1("hello"))









