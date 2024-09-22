# lib/shoe.py

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size
        self.condition = "Used"  # Default condition when the shoe is created

    # size property
    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            self._size = value
        else:
            print("size must be an integer")

    # cobble method
    def cobble(self):
        self.condition = "New"  # Set condition to "New" when cobble is called
        print("Your shoe is as good as new!")
