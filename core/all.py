from iterators import three_parts
from itertools import permutations
from utils import permute

class All:
    def __init__(self, n, m=None):
        if m is None:
            m = n
        self.n = n
        self.m = m
        poss = []
        for s in three_parts(n,m):
            for p in permutations(range(3)):
                poss.append(permute(s,p))
        self.poss = poss

    def __iter__(self):
        return iter(self.poss)

    def __getitem__(self, i):
        return self.poss[i]

    def contains(self, thing):
        tot = 0
        for a in thing:
            for b in a.matrix:
                tot += sum(b)
        if tot != self.n * self.m:
            return False
        for a in self:
            if a[0] == thing[0]:
                if a[1] == thing[1]:
                    if a[2] == thing[2]:
                        return True
                elif a[1] == thing[2]:
                    if a[2] == thing[1]:
                        return True
            elif a[0] == thing[1]:
                if a[1] == thing[0]:
                    if a[2] == thing[2]:
                        return True
                elif a[1] == thing[2]:
                    if a[2] == thing[0]:
                        return True
            elif a[0] == thing[2]:
                if a[1] == thing[0]:
                    if a[2] == thing[1]:
                        return True
                elif a[1] == thing[1]:
                    if a[2] == thing[0]:
                        return True
        return False

    def __len__(self):
        return len(self.poss)
