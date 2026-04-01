##Arrays (Level 2)

#1. second largest number

arr=[3,7,2,9,5]
large=arr[0]
second=arr[0]
for x in arr:
    if x > large:
        second=large
        large=x
    elif second<x and x!=large:
        second=x
print(second)


#2.Move all zeros to end

arr=[0,1,0,3,12]
non=[]
zero=[]
for x in arr:
    if x ==0:
        non.append(x)
    else:
        zero.append(x)
zero.extend(non)
print(zero)


#3.Count even and odd

arr=[1,2,3,4,5]
even=0
odd=0
for x in arr:
    if x % 2==0:
        even+=1
    else:
        odd+=1
print("Even",even)
print("Odd",odd)



