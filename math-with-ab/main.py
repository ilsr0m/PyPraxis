# put your python code here
class Mathematics:
    def __init__(self, val_a : int = 0, val_b: int = 0):
        self._a = val_a
        self._b = val_b

    @property
    def a(self):
        """Getter for a"""
        return self._a

    @a.setter
    def a(self, value):
        """Setter for a"""
        self._a = value

    @a.deleter
    def a(self):
        """Deleter for a"""
        del self._a

    @property
    def b(self):
        """Getter for b"""
        return self._b

    @b.setter
    def b(self, value):
        """Setter for b"""
        self._b = value

    @b.deleter
    def b(self):
        """Deleter for b"""
        del self._b

    def multiply(self):
        return self.a * self.b

    def divide(self):
        return self.a / self.b

    def subtract(self):
        return self.a - self.b

    def add(self):
        return self.a + self.b

    def divide_by_int(self):
        return int(self.a / self.b)

    def modulus(self):
        return self.a % self.b

    def square_root_of_sum(self, pow_value: int = 1):
        return (self.a ** pow_value + self.b ** pow_value) ** 0.5

op = Mathematics()
op.a = int(input())
op.b = int(input())

print(op.add())
print(op.subtract())
print(op.multiply())
print(op.divide())
print(op.divide_by_int())
print(op.modulus())
print(op.square_root_of_sum(10))

