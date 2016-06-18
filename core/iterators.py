from utils import rotate90, equ, eq1, to_int
from Shape import Shape

class three_parts:
    def __init__(self, n, m=None):
        if m is None:
            m = n
        self.shape = (n,m)
        self.n = n
        self.m = m
        self.current = None

    def __iter__(self):
        return self

    def next(self, check=True):
        if self.current is None:
            self.current = self.first()
        else:
            self.current[0][0] += 1
            i,j = 0,0
            while self.current[i][j] > 3:
                self.current[i][j] = 1
                i += 1
                if i >= self.m:
                    j += 1
                    i = 0
                    if j >= self.n:
                        raise StopIteration()
                self.current[i][j] += 1
        if check:
            while not self.is_max():
                self.next(False)
            print to_int(self.current)
            return self.three()

    def first(self):
        return [[1]*self.m for i in range(self.n)]

    def three(self):
        return [Shape(equ(self.current,i)) for i in range(1,4)]

    def is_max(self):
        p = self.current
        n = to_int(p)
        for i in range(3):
            p = rotate90(p)
            if len(p) == len(self.current) and to_int(p) > n:
                return False
        return True


