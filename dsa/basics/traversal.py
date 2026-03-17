#Traversal = visiting each element one by one

#Q1️⃣ Print all elements of array

arr=[10,20,30]
for i in range(len(arr)):
    print(arr[i])

#Q2️⃣ Print only numbers greater than 5

arr=[2,6,1,9,4]
for x in arr:
    if x >5:
        print(x)
#Q3️⃣ Print index and value together

arr=[4,7,1]
for i in range(len(arr)):
    print(i,arr[i])
#4.Q1️⃣ Print all elements using for-each

arr=[5,10,15]
for i in arr:
    print(i)

#5.Q2️⃣ Print index + value

arr=[8,3,6]
for x in range(len(arr)):
    print(x,arr[x])


#6.Q3️⃣ Count how many numbers are > 5
arr=[2,7,1,9,4]
count=0
for i in range(len(arr)):
               if arr[i]>5:
                   count+=1
print(count)
        

#7.Q4️⃣ Find first index of target

arr=[4,6,8,6]
target=6
for i in range(len(arr)):
    if arr[i]==target:
        print(i)
        break



#8.Q5️⃣ Find last index of target

arr=[4,6,8,6]
target=6
last_index=-1
for i in range(len(arr)):
    if arr[i]==target:
        last_index=i
        print(last_index)
        










