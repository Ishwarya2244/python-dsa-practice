arr=[8,3,6,1,5]
smallest=arr[0]
for i in range(len(arr)):
    if arr[i]<smallest:
        smallest=arr[i]
        position=i
print(smallest,position)
