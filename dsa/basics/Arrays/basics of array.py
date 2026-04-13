🧠 What is an Array?
An array is a collection of elements stored in a continuous memory location

🎒 Real-Life Example

Think of:
👉 A row of lockers
[ 3 ][ 1 ][ 4 ][ 2 ][ 5 ]
Each box = one element
All boxes are next to each other

💡 Key Properties

✔️ Same type of data (usually)
✔️ Stored continuously in memory
✔️ Access using index

🧠 How Array is Stored in Memory

👉 Suppose:

First element stored at memory address = 100
Each element takes 4 bytes

Memory Layout
Index   Value   Address
0        3       100
1        1       104
2        4       108
3        2       112
4        5       116

💡 Formula
👉 Address of element:

Base Address + (index × size)

👉 Example:
Index 2 → 100 + (2 × 4) = 108


⚙️ Basic Operations on Array

1️⃣ Access Element
arr[2]

👉 Time = O(1)

2️⃣ Traversal (Loop)
for i in arr:
    print(i)

👉 Time = O(n)

3️⃣ Insertion

👉 Insert at end:

arr.append(6)

👉 O(1)

👉 Insert at middle:

arr.insert(2, 10)

👉 Need to shift elements 😵
👉 Time = O(n)

4️⃣ Deletion
arr.remove(4)

👉 Shift elements
👉 Time = O(n)

5️⃣ Update
arr[1] = 10

👉 Direct replace
👉 Time = O(1)
arr=[3,1,4,2,5]

##logic:
        #Maximum
##    1.assign max variable as first element
##    2.loop throgh each element
##    3.check if current variable is greater than max if yes update
##    4.return max
##    Minimum
##    1.assign min variable as first element
##    2.loop throgh each element
##    3.check if current variable is less than min if yes update
##    4.return min
##    sum
##    1.assign total variable as zero
##    2.loop throgh each element
##    3.add each element with total to get sum 
##    4.return total

#Minimum
arr=[3,1,4,2,5]
minimum=arr[0]
for x in arr:
    if x < minimum:
        minimum=x
print(minimum)

#Maximum
arr=[3,1,4,2,5]
maximum=arr[0]
for x in arr:
    if x > maximum:
        maximum=x
print(maximum)

#Sum
arr=[3,1,4,2,5]
Total=0
for x in arr:
    Total+=x
print(Total)


#TIme complexity = O(n)
#space complexity = O(1)



