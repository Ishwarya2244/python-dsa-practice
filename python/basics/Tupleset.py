#TUPLE

numbers=(20,30,40,70)
print(numbers)

print(numbers[0])
print(numbers[2])
#numbers[0]=90#error bcz it's immutable(we can't cahnge once it assigns)


a=("shiv","div","char")
print(a[0])
print(a[-1])


mark=(9,80,90)
print(len(mark))#3

#SET
sets={20,200,30,40,20}
print(sets)

sets.add(80)
print(sets)

sets.remove(200)
print(sets)

sets.discard(40)
print(sets)


#set operations
a={1,2,3}
b={4,5,6}
print(a|b)#union(to combine)

a={90,90}
b={30,90}
print(a&b)#intersection (common)

x={2,3,4,5}
y={5,4,6,7}
print(x-y)#difference#2,3
print(y-x)#6,7


number={20,30,20,40,50,60,60}
print(number)

a = {1, 2, 3}
b = {3, 4}
print(a|b)
print(a&b)







