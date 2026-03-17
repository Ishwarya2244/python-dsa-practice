name = "Aishu"
print(name[0])#A
print(name[-1])#u
print(name[-5:-2])#Ais
print(name[:3])
print(name[3:])

name=input("enter name:")
print(name[0])
print(name[-1])
print(name[1:-1])

print(name.lower())
print(name.upper())
print(name.find("A"))
print(name.replace("w","e"))
print(name.strip())
print(len(name))

girl=input("enter your name:")
print(len(girl))
print(girl.upper())
#print(girl.replace([0],"*"))
print("*" + girl[1:])
print(girl[1:-1])
print(girl.find("z"))



#LOGIc

arr=list(map(int,input("enter numbers:").split()))
to_delete=int(input("enter a number to delete:"))
if to_delete in arr:
    arr.remove(to_delete)
    print(arr)
else:
    print("Cannot delete, element not found")


arr=list(int(input("enter list:")))
print(arr)








