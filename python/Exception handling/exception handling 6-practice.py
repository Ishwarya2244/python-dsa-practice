##Day 6 Practice Questions
##Question 1
##
##Write a program that:
##
##asks user for a number
##prints "Invalid Input" if user enters text
##
##Use:
##try
##except

try:
    num=int(input("enter a number:"))
    print(num)
except ValueError:
    print("Invalid Input")

##Question 2
##Handle this error:
##result = 20 / 0
##Print:
##Cannot divide by zero

try:
    result=20/0
    print(result)
except ZeroDivisionError:
    print("Cannot divide by zero")


##Question 3
##Use:
##try
##except
##else
##If user enters a valid number, print:
##Number accepted


try:
    num=int(input("enter a number:"))
except ValueError:
    print("Invalid Number")
else:
    print("Number accepted")


##Question 4
##Use:
##try
##except
##finally
##Print:
##Program Finished
##in the finally block.


try:
    num=int(input("enter ur num:"))
    print(num)
except ValueError:
    print("Invalid number")
finally:
    print("program finished")



except runs when an error occurs
else runs when no error occurs




