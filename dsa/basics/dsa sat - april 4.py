#Arrays

#Sum of all elements

arr=[4,2,7,1]
total=0
for x in arr:
    total+=x
print(total)


#Find largest element

arr=[10,5,8,20,3]
large=arr[0]
for x in arr:
    if x>large:
        large=x
print(large)



#check if array is sorted(ascending)

arr=[1,2,3,4]
sorted=True
for i in range(len(arr)-1):
    if arr[i] > arr[i+1]:
        sorted=False
        break
print(sorted)
        
        
    


#find second largest element

arr=[12,35,1,10,34,1]
large=arr[0]
second=arr[0]
for x in arr:
    if x > large:
        second=large
        large=x
    elif x>second and x!=large:
        second=x
print(second)


#move all zeros to end

arr=[0,1,0,3,12]
arr1=[]
arr2=[]
for x in arr:
    if x == 0:
        arr1.append(x)
    else:
        arr2.append(x)
arr2.extend(arr1)
print(arr2)




















    
        
