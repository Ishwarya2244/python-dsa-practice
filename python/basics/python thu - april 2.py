#1Print all elements using index

arr=[2,4,6,8]
for i in range(len(arr)):
    print(i,arr[i])

# Add element 10 to list and print


arr=[2,4,6,8]
arr.append(10)
print(arr)

#3.
arr.remove(arr[-1])
print(arr)


#5.Count how many elements are greater than 5

arr=[2,7,4,9,1]
count =0
for x in arr:
    if x > 5:
        count+=1
print(count)


#4. 👉 Find sum of all elements using index

arr=[2,4,6,8]
total=0
for i in range(len(arr)):
    total+=arr[i]
print(total)





