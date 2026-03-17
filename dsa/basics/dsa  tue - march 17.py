# find frequency of elements in a list

list1=[1,2,2,3,1,1]
freq={}
for x in list1:
    if x in freq:
        freq[x]+=1
    else:
        freq[x]=1
print(freq)


#find the first non-repeating element in a list

list1=[1,2,2,3,1,4]
freq={}
for x in list1:
    if x in freq:
        freq[x]+=1
    else:
        freq[x]=1
for x in list1:
    if freq[x]==1:
        print(x)
        break

