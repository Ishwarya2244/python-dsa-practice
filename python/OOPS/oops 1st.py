class Book:
    def show_title(self):
        print(self.title)
book1=Book()
book1.title="Python Basics"
book1.show_title()


class Student:

    def show_name(self):  #✅ self refers to student1
        print(self.name)

student1 = Student()

student1.name = "Ishu"
student1.show_name()


##One More Tiny Practice
##
##Try this completely by yourself:
##
##Task
##
##Create a class called:
##
##Car
##
##Create an object:
##
##my_car
##
##Add an attribute:
##
##brand = "Toyota"
##
##Create a method:
##
##show_brand
##
##that prints the brand.
##Then call the method.


class Car:
    def show_brand(self):
        print(self.brand)
my_car=Car()
my_car.brand="Toyota"
my_car.show_brand()

Car = Class

my_car = Object

brand = Attribute

Toyota = Value

show_brand = Method

self = Current object
