from Code.complex_class import *

 
class Quaternion:
    def __init__(self, elements):
        self.elements = elements
        if len(elements) != 4:
            error("Quaternions must be given 4 elements")
            raise DimensionError

    def show(self):
        q = ''
        p = []
        for i in range(len(self.elements)):
            if i == 0:
                p.append('')
            else:
                p.append('e' + str(i))
        for x in range(len(self.elements)):
            z = self.elements[x]
            if z > 0:
                if x != 0:
                    q += ' + '
                q += str(z) + p[x]
            elif z < 0:
                if x != 0:
                    q += ' - '
                q += str(-z) + p[x]
        print(q)

    def add(self, other):
        if type(other) in [int, float]:
            [r, i, j, k] = [x + other for x in self.elements]
            return Quaternion([r, i, j, k])
        elif type(other) == Quaternion:
            [r, i, j, k] = [x + y for x, y in zip(self.elements, other.elements)]
            return Quaternion([r, i, j, k])
        elif type(other) == Complex:
            other = complex_to_quaternion(other)
            return self.add(other)

    def mult(self, other):
        if type(other) in [int, float]:
            [r, i, j, k] = [x * other for x in self.elements]
            return Quaternion([r, i, j, k])
        elif type(other) == Quaternion:
            [a1, b1, c1, d1] = self.elements
            [a2, b2, c2, d2] = other.elements
            r = a1 * a2 - b1 * b2 - c1 * c2 - d1 * d2
            i = a1 * b2 + b1 * a2 + c1 * d2 - d1 * c2
            j = a1 * c2 - b1 * d2 + c1 * a2 + d1 * b2
            k = a1 * d2 + b1 * c2 - c1 * b2 + d1 * a2
            return Quaternion([r, i, j, k])
        elif type(other) == Complex:
            other = complex_to_quaternion(other)
            return self.mult(other)

    def norm(self):
        q = [x ** 2 for x in self.elements]
        return math.sqrt(sum(q))

    def conjugate(self):
        [r, i, j, k] = [-x for x in self.elements]
        r *= - 1
        return Quaternion([r, i, j, k])


def complex_to_quaternion(z):
    if type(z) == Complex:
        return Quaternion([z.re, z.im, 0, 0])
