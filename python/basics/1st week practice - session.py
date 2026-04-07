##1. What is a variable ?
##
##variable is container to store a values . example : a=0, a is a variable
##
##2. Take a number from user and print:
##
a=int(input("enter a:"))
if a>0:
    print("positive")
elif a<0:
    print("negative")
elif a==0:
    print("zero")
else:
    print("none")


##Q3️⃣ Print numbers from 1 to 10, but skip 4 and 7

for i in range(1,11):
    if i==4:
        continue
    if i==7:
        continue
    print(i)



#4.Print numbers from 5 to 1 using while

i=5
while i >0:
    print(i)
    i-=1


##Q5️⃣ Print numbers from 1 to 10
##
##👉 Stop when number is 6


for i in range(1,11):
    if i == 6:
        break
    print(i)



##Q6️⃣ Count how many numbers are odd


arr=[2,5,7,8,9,10]
count=0
for x in arr:
    if x%2!=0:
        count+=1
print(count)



##Q6️⃣ Count how many numbers are odd


for i in range(1,5):
    print("*"*i)






    
