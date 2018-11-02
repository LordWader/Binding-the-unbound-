from math import hypot

class Vector:
    """
    This program presents a naive implementation of a two-dimensional vector
    with some basic operations like: multiplying vector by scalar, adding two vectors,
    calculation the length of a vector and a string representation of the vector.
    If user enter any other function, the program will return the name of the entered function.
    by Nick Proshin
    """
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def abs(self):
        """
        Return the length of Vector
        """
        return hypot(self.x, self.y)
        
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        """
        Returns the result of multiplying a vector by a number
        """
        return Vector(self.x*scalar, self.y*scalar)

    def __repr__(self):
        return 'Vector(%s, %s)' % (self.x, self.y)
    
    def bind(self, as_name):
        setattr(self, as_name, (lambda pop: print(as_name)).__get__(self, self.__class__))
        
    def __getattr__(self, name):
        """
        >>> a = Vector(3, 4)
        >>> a.fruit()
        fruit
        >>> a.car(300, 400, 'spam')
        car
        """
        self.bind(name)
        func_name = self.__getattribute__(name)
        return func_name


if __name__=="__main__":
    a = Vector(1, 1)
    print(a.abs())
    a.foo()
    print(a.__dict__)
    a.foo()
    a.kek()
    a.car()
    print(a.foo)
    print(a.kek)
    print(a.car)
