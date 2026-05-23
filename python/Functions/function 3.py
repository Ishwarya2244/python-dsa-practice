##🚀 Day 3 → Dictionaries + Real-world Data Handling
##
##Dictionaries in Python
##
##Dictionaries are used everywhere in real-world programming:
##
##APIs
##JSON
##AI/Data Science
##Backend development
##Databases
##Web applications
##
##If lists store multiple values,
##then dictionaries store data in:
##
##key → value format
##
##Part 1 — What is a Dictionary?
##
##A dictionary stores data using keys and values.
##
##Example
##student = {
##    "name": "Ishu","age": 20,
##    "course": "AI & DS"
##}
##
##print(student)
##
##Part 2 — Accessing Values
##
##We access values using keys.
##
##Part 3 — Adding New Data
##
##part 4 - updating value
##
##Part 5 — Looping Through Dictionary
##Print keys
##student = {
##    "name": "Ishu",
##    "age": 20
##}
##
##for key in student:
##    print(key)



##Day 3 Practice Questions
##Question 1
##Create a dictionary for a car with:
##
##brand
##model
##year
##
##Then print the entire dictionary.


car={
    'brand':'Rocky',
    'model':'benz',
    'year':2026
}
print(car)


##Question 2
##
##Create a student dictionary and print only the student's name.

student={
    'name':'Ishwarya',
    'dept':'AIDS',
    'college':'ACE'
}
print(student['name'])


##Question 3
##Add a new key called:
##"city"
##to a dictionary.

student['city']='Hosur'
print(student)

##Question 4
##Update the age in this dictionary:
##person = {
##    "name": "Ram",
##    "age": 18
##}
##Change age to:
##19

person = {
    "name": "Ram",
    "age": 18
}
person['age']=19
print(person)


##Question 5
##Loop through this dictionary and print all values.
##employee = {
##    "name": "John",
##    "role": "Developer",
##    "salary": 50000
##}

employee = {
    "name": "John",
    "role": "Developer",
    "salary": 50000
}

for key in employee:
    print(employee[key])


