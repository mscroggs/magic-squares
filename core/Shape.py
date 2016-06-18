from utils import rotate90, char

class Shape:
    def __init__(self, matrix):
        self.matrix = matrix

    def __eq__(self, other):
        for rot in self.rotations():
            if rot == other.matrix:
                return True
        return False

    def rotations(self):
        rots = [self.matrix]
        for i in range(3):
            rots.append(rotate90(rots[-1]))
        return rots

    def __unicode__(self):
        out = ""
        out += " " + "-"*len(self.matrix[0]) + " "
        out += "\n"
        for row in self.matrix:
            out += "|"
            out += "".join([char(i) for i in row])
            out += "|"
            out += "\n"
        out += " " + "-"*len(self.matrix[0]) + " "
        return out

    def __str__(self):
        return unicode(self).encode('utf-8')
