##What is Array Deletion?
##
##👉 Removing an element from an array by index or value.

#pop(index) → deletes by index

#remove(value) → deletes first occurrence

##🔴 Time Complexity (simple)
##
##Deletion using search → O(n)
##Because we may check every element.


#Q1️Delete element at index 1
arr=[4,8,6,9]
arr.pop(1)
print(arr)

#Delete value 7

arr=[3,7,1,7,9]
arr.remove(7)
print(arr)




#Q3️⃣ (logic)Delete last occurrence of 2

arr=[5,2,3,2,9]
target=2
last_value=-1
for i in range(len(arr)):
    if arr[i]==target:
        last_value=i
if last_value !=-1:
            print(arr.pop(last_value))
else:
  print("not found")


#4.Delete first occurrence of 4:

arr=[1,4,3,4,5]
target=4
for i in range(len(arr)):
    if arr[i]==target:
        arr.pop(i)
        break
print(arr)


#5.Delete last occurrence of 7:

arr=[7,2,7,4,7]
last_index=-1
target=7
for i in range(len(arr)):
    if arr[i]==target:
        last_index=i
if last_index !=-1:
    print(arr.pop(last_index))
else:
    print("not found")



arr=[7,2,7,4,7]
last_index=-1
target=7
for i in range(len(arr)):
    if arr[i]==target:
        last_index=i
        print(last_index)
    else:
        print(-1)






















    
    
        
