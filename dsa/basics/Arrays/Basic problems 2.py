##1.Check if a given number exists in array
##
arr=[8,2,3,4]
target=3
if target in arr:
        print(True)
else:
  print(False)

###Logic:
##  1.assign exist number
##  2.check condition
##  3.if have return true else false
##  
#time=O(1)
#space=O(1)


#2.Count how many numbers are greater than X

##logic:
##    1.assgin count =0 and also x
##    2.loop through each element
##    3.check condition if current element is greater than asssigned element increse count by 1
##    4.return count
##
##time=O(n)
##space=O(1)

arr=[2,3,4,5,4]
count=0
x=1
for i in arr:
    if i > x:
        count+=1
print(count)


#3.Replace all negative numbers with 0
##
##logic:
##    1.

##arr=[2,4,-1,3,-4]
##rep=[]
##for x in arr:
##    if x<0:
##        x.insert(0)
##print(x)



#4.Reverse the array without built in

arr=[3,2,1,4]
print(arr[::-1])








