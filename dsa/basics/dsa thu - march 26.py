#Sorting

#1.Bubble sort ascending

#ascending order using bubble sort

arr=[6,3,9,1]
for i in range(len(arr)):
    for j in range(len(arr)-1):
        if arr[j]> arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
print(arr)


#2.Check if list is sorted

#Check if list is alreasy sorted(ascending)

arr=[3,1,2]
is_sorted=True
for i in range(len(arr)-1):
    if arr[i]>arr[i+1]:
        is_sorted=False
        break
print(is_sorted)

#
arr=[1,2,3,4]
is_sorted=True
for i in range(len(arr)-1):
    if arr[i]>arr[i+1]:
        is_sorted=False
        break
print(is_sorted)
