#Arrays


#1. find minimum element in a list

a=[9,8,6,4,3,2]
minimum=a[0]
for x in a:
    if x < minimum:
        minimum=x
print(minimum)


#2. find sum of all elements

a=[9,8,6,4,3,2]
total=0
for x in a:
    total+=x
print("sum of all elements:",total)


#3. find second smallest element

a=[9,8,6,4,3,2]
small=a[0]
second=a[0]
for x in a:
    if x < small:
        second=small
        small=x
    elif x<second and x!=small:
        second=x
print(second)
        

#4. move all zeros to end


list1=[0,1,0,3,12]
a=[]
b=[]
for x in list1:
    if x>0:
        a.append(x)
    else:
        b.append(x)
a.extend(b)
print(a)



#Sorting

arr=[10,5,8]
for i in range(len(arr)-1):
    print(arr[i],arr[i+1])


#Sort a list in ascending order using bubble sort

arr=[5,2,8,1]
for i in range(len(arr)):
    for j in range(len(arr)-1):
        if arr[i]>arr[j+1]:
            swap
            print(j)








