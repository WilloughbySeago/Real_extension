from Code.errors import *
import math


class Complex:
    """This is a class of complex numbers"""
    def __init__(self, re, im):
        """
        Initialise the complex number
        :param re: real number
        :param im: real number
        """
        self.re = re
        self.im = im

    def is_real(self):
        """
        Returns whether or not a number is real
        :return: bool
        """
        return not bool(self.re)

    def show(self):
        """
        prints the number
        :return: None
        """
        if self.im > 0:
            print(f"{self.re} + {self.im}i")
        elif self.im > 0:
            print(self.re)
        else:
            print(f"{self.re} - {-self.im}i")

    def add(self, other):
        """
        adds self and other
        :param other: complex number
        :return: Complex
        """
        if type(other) in [int, float]:
            return Complex(self.re + other, self.im)
        elif type(other) == Complex:
            return Complex(self.re + other.re, self.im + other.im)
        else:
            error("Cannot add those types together")
            raise TypeError

    def mult(self, other):
        """
        multiples self and other
        :param other: complex number
        :return: Complex
        """
        if type(other) in [int, float]:
            return Complex(self.re * other, self.im * other)
        elif type(other) == Complex:
            real = self.re * other.re - self.im * other.im
            imag = self.re * other.im + self.im * other.re
            return Complex(real, imag)

    def sub(self, other):
        """
        Subtracts other from self
        :param other: complex number
        :return: Complex
        """
        if type(other) in [int, float]:
            return self.add(- other)
        elif type(other) == Complex:
            return self.add(Complex(-other.re, -other.im))

    def mod(self):
        """
        returns |self|
        :return: real number
        """
        return math.sqrt(self.re ** 2 + self.im ** 2)

    def arg(self):
        """
        returns arg(self)
        :return: real number in [-pi, pi]
        """
        return math.atan2(self.re, self.im)

    def conjugate(self):
        return Complex(self.re, -self.im)


def from_euler(mod, arg):
    """
    This is a function that creates a complex number from its modulus and argument
    :param mod: real number
    :param arg: real number
    :return: Complex
    """
    return Complex(mod * math.cos(arg), mod * math.sin(arg))
