from math import hypot
import types

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
        >>> a = Vector(3, 4)
        >>> a.abs()
        5.0
        """
        return hypot(self.x, self.y)
        
    def __add__(self, other):
        """
        >>> a = Vector(3, 4)
        >>> b = Vector(1, 2)
        >>> a + b
        Vector(4, 6)
        """
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        """
        Returns the result of multiplying a vector by a number
        >>> a = Vector(3, 4)
        >>> scalar = 10
        >>> a*scalar
        Vector(30, 40)
        """
        return Vector(self.x*scalar, self.y*scalar)

    def __repr__(self):
        """
        >>> a = Vector(y = 1)
        >>> print(a)
        Vector(0, 1)
        """
        return 'Vector(%s, %s)' % (self.x, self.y)    
        
    @classmethod    
    def bind(cls, as_name):
        setattr(cls, as_name, (lambda pop: print(as_name)).__get__(cls, cls))
        
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
    a.abs()
    print(a.abs())
    a.foo()
    a.foo()
    a.kek()
    a.car()
    print(a.foo)
    print(a.kek)
    print(a.car)
    a.car()
    print(dir(Vector))
    print(Vector.foo)
