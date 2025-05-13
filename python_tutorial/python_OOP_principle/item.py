import csv

class Item:
    pay_rate = 0.8 # The pay rate after 20% discount
    all = []

    # "__" --> this is called Dunder
    # __init__ --> this is the Constructor of any Class
    def __init__(self, name: str, price: float, quantity=0):
        # Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater or equal to zero!"

        # Assign to self object
        self.__name = name
        self.__price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    # Property Decorator = Read-Only Attribute
    # "getter()" method er moto
    # "__price" is used so that No One Outside the Class Can Access the Property(Private Variable)... and as "@property" variable is Read-Only... That's why "item.price=30" can't be Set...So, that's how we make it a "Setter" Function & Read-Only
    @property
    def price(self):
        return self.__price

    def apply_discount(self):
        self.__price = self.__price * self.pay_rate

    def apply_increment(self, increment_value):
        self.__price = self.__price + self.__price * increment_value


    # Property Decorator = Read-Only Attribute
    # "getter()" method er moto
    # "__name" is used so that No One Outside the Class Can Access the Property(Private Variable)... and as "@property" variable is Read-Only... That's why "item.name=Laptop6" can't be Set...So, that's how we make it a "Setter" Function & Read-Only
    @property
    def name(self):
        return self.__name

    # "setter()" method er moto
    # As why "item.name=Laptop6" can't be Set & "__name" is Private Variable... so, to set the value we need "@name.setter"
    # "@property_variable_name.setter" --> this is the Syntax
    @name.setter
    def name(self, value):
        if len(value) > 10:
            raise Exception("The name is too long!")
        else:
            self.__name = value

    def calculate_total_price(self):
        return self.__price * self.quantity

    # "cls" Parameter is Passed Automatically
    # We use "@classmethod" to Instantiate the Object of that Class
    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),
            )

    # We use "@staticmethod" to any Common/Util Function Applicable to all the Instance of that Class
    @staticmethod
    def is_integer(num):
        # We will count out the floats that are point zero
        # For i.e: 5.0, 10.0
        if isinstance(num, float):
            # Count out the floats that are point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    # Print Function first checks if __str__(self) is available & if Not available then it checks the output "__repr__(self)"... if both of them is not available then it print the Generic Object as String with Memory Location
    def __str__(self) -> str:
        # " -> str" this mean, "string" is the Return Type
        return f"{self.name} --> Price: {self.price}, Quantity: {self.quantity}"

    # __repr__ is used for Developer to see the Object Representation... We can use the Object's "Constructor" Format here. So that we can easily Copy it's Output... it is usually used in "Python Console"... When we type only the OBJECT... without Print Function this will Print it
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.name}', {self.__price}, {self.quantity})"


# This Code will Only be Run if this ".py" is Executed... If the Item.py is imported from Another Class it won't be executed
if __name__ == "__main__":

    p1 = Item("Laptop", 2000, 1)
    p2 = Item("PC", 1500, 1)
    p3 = Item("Mobile", 600, 1)

    print(p1)
    print(p2)
    print(p3)