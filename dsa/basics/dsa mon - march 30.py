#ARRAY

#Print all elements using loop

arr=[5,10,15,20]
for x in arr:
    print(x)

#print elements using index

arr=[5,10,15,20]
for i in range(len(arr)):
    print(i,arr[i])


#print sum of all elements


arr=[5,10,15,20]
total=0
for x in arr:
    total+=x
print(total)


#👉 Find maximum element

arr=[5,10,15,20]
maxi=arr[0]
for x in arr:
    if x>maxi:
        maxi=x
print(maxi)


#👉 Find minimum element

arr=[5,10,15,20]
mini=arr[0]
for x in arr:
    if x<mini:
        mini=x
print(mini)



#🔴 Q6: Check if array is sorted

arr=[3,1,2]
is_sorted=True
for i in range(len(arr)-1):
    if arr[i]>arr[i+1]:
        is_sorted=False
        break
print(is_sorted)
















