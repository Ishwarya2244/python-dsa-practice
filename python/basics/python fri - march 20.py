#String + logic

#1.
# remove all vowels from a string

string="aishu"
vowels='a','e','i','o','u'
s=""
for x in string:
   if x not in vowels:
      s+=x
   else:
        continue
print(s)
        

#2.

#palindrome

char="fales"
reversed_string=char[::-1]
print(reversed_string)
if char==reversed_string:
      print(True)
else:
     print(False)


#string splitting + word logic


# *.split()

# 1* first step= split(), 2* loop words  3* apply logic

#problem 1

#count number of words

word="I love python"
s=word.split()
count=0
for x in s:
    count+=1
print(count)


#2. print each word in new line

word1="I love python"
new=word1.split()
for x in new:
    print(x)













