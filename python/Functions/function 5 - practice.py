##Day 5 Practice Questions
##Question 1
##Create a file named:
##notes.txt
##Write:
##Python is easy to learn
##into it.

file=open("notes.txt",'w')
content=file.write("Python is easy to learn")
file.close()


##Question 2
##Read the content from:
##notes.txt
##and print it.
file=open("notes.txt",'r')
content=file.read()
print(content)
file.close()

##Question 3
##Append this line into the file:
##I am practicing Python daily

file=open("notes.txt",'a')
file.write("\nI am practicing python daily")
file.close()

##
##Question 4
##Create a program that takes user input and stores it in a file.
##Example:
##Enter your name:
##Store that name inside a file.

name=input("Enter your name:")
file=open("notes.txt","w")
file.write(name)
file.close()
print("Name stored successfully")
















