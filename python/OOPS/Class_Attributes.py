PYTHON DAY 14 - CLASS ATTRIBUTES

A class attribute is shared by all objects of a class.

Example:

class Employee:

    company = "OpenAI"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_details(self):
        print(self.name)
        print(self.salary)
        print(Employee.company)

employee1 = Employee("Ishu", 25000)

employee1.show_details()

Output:

Ishu
25000
OpenAI

Important:

Class Attribute:
company

Instance Attributes:
name
salary

Object:
employee1

Class attributes are shared by all objects.
Instance attributes belong to individual objects.
