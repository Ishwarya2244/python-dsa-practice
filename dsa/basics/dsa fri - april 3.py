##Pattern + Thinking Problems
##Q1: First Non-Repeating Element


arr=[1,2,2,3,1,4]
fre={}
for x in arr:
    if x in fre:
        fre[x]+=1
    else:
        fre[x]=1
for x in arr:
    if fre[x] == 1:
        print(x)
        break


#Q2: Remove Duplicates

arr=[1,2,2,3,1,4]
seen=set()
result=[]
for x in arr:
    if x not in seen:
        seen.add(x)
        result.append(x)
print(result)

#3. Two sum

arr = [2,7,11,15]
target = 9

seen = set()

for x in arr:
    needed = target - x
    
    if needed in seen:
        print(x, needed)
        break
    
    seen.add(x)














