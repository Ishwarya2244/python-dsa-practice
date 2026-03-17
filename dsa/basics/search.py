
      #day 2

#1.Given a list of numbers, check whether the target number is present or not.
#If present, print "Yes", else print "No".

arr=[3,6,9,2]
target = 6
if target  in arr:
    print("yes")
else:
    print("no")


#2.Find the index of a target number using linear search.
#If not found, print -1.

arr=[10,20,30,40]
target = 50
if target in arr:
    print("found")
else:
    print(-1)

# LINEAR SEARCH
#checking each element by one by one until the target is found
#we use linear search when array or list is unsorted ,small data

    
#Time complexity
#How much time an algorithm takes when input size increases
#⚠️ Not clock time
#⚠️ Not seconds or minutes

#It is about number of steps your code takes.


##✔ Best Case
##
##Element at first index
##
##Checks = 1
##👉 O(1)
##
##❌ Worst Case
##
##Element at last / not present
##
##Checks = n
##👉 O(n)
##
##🔁 Average Case
##
##Somewhere in middle
##👉 O(n)



# 1. Find target in list and print index if found, else print -1

arr=[5,8,2,9]
target=2
for i in range(len(arr)):
    if arr[i]==target:
        print(i)
        break
else:
  print(-1)


# 2. Count how many times target appears
arr=[1,2,3,2,2,5]
target=2
count=0
for  i in range(len(arr)):
    if arr[i]==target:
        count+=1
print(count)
       

#3.Find the first index of target, else print -1

arr=[4,7,1,7,9]
target=7
for i in range(len(arr)):
    if arr[i]==target:
        print(i)
        break
else:
    print(-1)
               

#4.Find the last index of target, else print -1
arr=[5,2,3,2,9]
target=2
last_index=-1
for i in range(len(arr)):
    if arr[i]==target:
        last_index=i
if last_index==-1:
    print("not found")
else:
    print(last_index)
        
    
#5.
arr=[4,7,1,7,9]
target=7
for i in range(len(arr)):
    if arr[i]==target:
        print(i)
        break
else:
    print(-1)

#6.
arr=[1,3,5,3,9,3]
target=3
last_index=-1
for i in range(len(arr)):
    if arr[i]==target:
        last_index=i
if last_index==-1:
    print("not found")
else:
    print(last_index)



  
