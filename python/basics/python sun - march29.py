#STRING

string="hello"
for x in string:
    print(x)

#count digits

string="a1b2c3"
digit='1','2','3'
count=0
for x in string:
    if x in digit:
        count+=1
print(count)


string="a1b2c3"
count=0
for x in string:
    if x >='0' and x<='9':
        count+=1
print(count)


string="a1b2c3"
count=0
for x in string:
    if (x>='a' and x<='z')or(x>='A' and x<='Z'):
        count+=1
print(count)


string="aabbc"
s=set()
for x in string:
    if x in s:
        print(x)
        break
    else:
        s.add(x)        


#ANAGRAM

s1="listen"
s2="silent"
if sorted(s1)==sorted(s2):
    print(True)
else:
    print(False)


string="aabbcc"
dic={}
for x in string:
    if x in dic:
        dic[x]+=1
    else:
       dic[x]=1
print(dic)
















