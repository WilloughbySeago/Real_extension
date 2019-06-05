from quaternion_class import *


class Octonion:
    def __init__(self, elements):
        self.elements = elements
        if len(self.elements) != 8:
            error('Octonions must have 8 components')
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

    def norm(self):
        q_squared = [x ** 2 for x in self.elements]
        return math.sqrt(sum(q_squared))

    def conjugate(self):
        q = []
        for i in range(len(self.elements)):
            if i == 0:
                q.append(self.elements[i])
            else:
                q.append(-self.elements[i])
        return Octonion(q)

    def add(self, other):
        if type(other) in [int, float]:
            q = [x + other for x in self.elements]
            return Octonion(q)
        elif type(other) == Complex:
            other = complex_to_octonion(other)
            return self.add(other)
        elif type(other) == Quaternion:
            other = quaternion_to_octonion(other)
            return self.add(other)
        elif type(other) == Octonion:
            q = [x + y for x, y in zip(self.elements, other.elements)]
            return Octonion(q)


def quaternion_to_octonion(z):
    return Octonion(z.elements + [0, 0, 0, 0])


def complex_to_octonion(z):
    z = complex_to_quaternion(z)
    z = quaternion_to_octonion(z)
    return z


z = Octonion([1, 2, 3, 4, 5, 6, 7, 8])
w = Octonion([5, 4, 7, 2, 9, 3, 7, 2])
z.add(w).show()

