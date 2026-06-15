 - MULTIPLE METHODS

A class can have more than one method.
practice:
Example:

class Mobile:

    def __init__(self, brand):
        self.brand = brand

    def show_brand(self):
        print(self.brand)

    def ring(self):
        print(self.brand, "is ringing")

mobile1 = Mobile("Vivo")

mobile1.show_brand()
mobile1.ring()

Output:

Vivo
Vivo is ringing

Important:

A class can contain multiple methods.

Methods can use attributes stored in the object.

Object:
mobile1

Attribute:
brand

Methods:
show_brand()
ring()
