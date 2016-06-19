from utils import rotate90, char, replace, ascii_char
from itertools import permutations

class Shape:
    def __init__(self, matrix):
        while False not in [i==0 for i in matrix[0][:]]:
            matrix = matrix[1:][:]
        while False not in [i==0 for i in matrix[-1][:]]:
            matrix = matrix[:-1][:]
        while False not in [i==0 for i in matrix[:][0]]:
            matrix = matrix[:][1:]
        while False not in [i==0 for i in matrix[:][-1]]:
            matrix = matrix[:][:-1]
        self.matrix = matrix

    def __eq__(self, other):
        for rot in self.rotations():
            if rot == other.matrix:
                return True
        return False

    def rotations(self):
        rots = [self.matrix]
        for i in range(3):
            base = rotate90(rots[-1])
            for p in permutations(range(1,4)):
                rots.append(replace(base,p))
        return rots

    def __unicode__(self):
        out = ""
        for row in self.matrix:
            out += "".join([char(i) for i in row])
            out += " "
            out += "\n"
        return out

    def __str__(self):
        return unicode(self).encode('utf-8')

    def to_ascii(self):
        out = ""
        for row in self.matrix:
            out += "".join([ascii_char(i) for i in row])
            out += " "
            out += "\n"
        return out
