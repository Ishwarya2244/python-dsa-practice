#Basic problems on Array

#1. print all elements of array

##Logic :
##    1.loop through each element
##    2.return one by one
##Time complexity =O(n)
##space complexity =O(1)

arr=[3,4,5,6]
for x in arr:
    print(x)

#2. Find sum of all elements
##
##Logic:
##    1.assign toal as 0
##    2.loop through each element
##    3.add each element with total
##    4. return total
##time complexity=O(n)
##space complexity =O(1)

arr=[3,4,5,6]
total=0
for x in arr:
    total+=x
print(total)



#3.
arr=[3,1,4,2,5]

##logic:
        #Maximum
##    1.assign max variable as first element
##    2.loop throgh each element
##    3.check if current variable is greater than max if yes update
##    4.return max
##
##Time complexity =O(n)
##space complexity =O(1)

#Maximum
arr=[3,1,4,2,5]
maximum=arr[0]
for x in arr:
    if x > maximum:
        maximum=x
print(maximum)


#4. find minimum element
##LOgic
##    Minimum
##    1.assign min variable as first element
##    2.loop throgh each element
##    3.check if current variable is less than min if yes update
##    4.return min

##Time complexity =O(n)
##space complexity =O(1)

#Minimum
arr=[3,1,4,2,5]
minimum=arr[0]
for x in arr:
    if x < minimum:
        minimum=x
print(minimum)


#5.Count how many elements are even

##Logic:
##    1.assign count=0
##    2.loop through each element
##    3.check if elements are even count increases by 1
##    4.return count
##time=O(n)
##space=O(1)

arr=[3,2,1,4,5]
count=0
for x in arr:
    if x %2==0:
        count+=1
print(count)


#6.Count how many elements are odd


##Logic:
##    1.assign count=0
##    2.loop through each element
##    3.check if elements are odd count increases by 1
##    4.return count
##time=O(n)
##space=O(1)


arr=[3,2,1,4,5]
count=0
for x in arr:
    if x %2!=0:
        count+=1
print(count)



#7.Find average of elements

##logic:
##    1.loop through each element
##    2.formula for avereage average=sum(arr)/len(arr)
##    3.return average
##time=O(n)
##space=O(1)


arr=[3,4,2,5]
total=0
for x in arr:
    total+=x
    average=total/len(arr)
print(average)










