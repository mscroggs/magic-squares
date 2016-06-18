from iterators import three_parts
from itertools import permutations
from utils import permute

class All:
    def __init__(self, n, m=None, output=False):
        if m is None:
            m = n
        self.n = n
        self.m = m
        poss = []
        poss2 = []
        for s in three_parts(n,m,output=output):
            for p in permutations(range(3)):
                poss.append(permute(s,p))
            for p in [(0,1,2),(0,2,1)]:
                poss2.append(permute(s,p))
        self.poss = poss
        self.poss_short = poss2

    def __iter__(self):
        return iter(self.poss)

    def __getitem__(self, i):
        return self.poss[i]

    def contains(self, thing):
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
