from Shape import Shape

class three_parts:
    def __init__(self, n, m=None):
        if m is None:
            m = n
        self.shape = (n,m)
        self.current = None

    def __iter__(self):
        return self

    def next(self):
        if self.current is None:
            self.current = self.first()
        else:
            pass
        return self.three()

    def first(self):
        arr = [[1]]

    def three(self):
