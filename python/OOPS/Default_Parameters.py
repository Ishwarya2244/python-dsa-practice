PYTHON DAY 15 - DEFAULT PARAMETERS

Default parameters allow a value to be used automatically if no value is provided.

Example:

class Person:

    def __init__(self, name="Guest"):
        self.name = name

    def show_name(self):
        print(self.name)

person1 = Person()
person2 = Person("Ishu")

person1.show_name()
person2.show_name()

Output:

Guest
Ishu

Important:

Default Value:
"Guest"

Object 1:
person1

Object 2:
person2

If no value is passed, the default value is used.
If a value is passed, that value is used.
