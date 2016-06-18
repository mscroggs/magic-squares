def rotate90(matrix):
    return [[row[-1-i] for row in matrix] for i in range(len(matrix[0]))]

def char(i):
    if i==0:
        return " "
    if i==1:
        return u"\u2588"
    if i==2:
        return u"\u259B"
    if i==3:
        return u"\u259F"
    if i==4:
        return u"\u259C"
    if i==5:
        return u"\u2599"

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
