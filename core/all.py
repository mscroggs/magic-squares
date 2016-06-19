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
            poss.append(s)
            if s[0] != s[1]:
                poss.append(permute(s,(1,0,2)))
            if s[0] != s[2]:
                poss.append(permute(s,(2,1,0)))
            if s[1] != s[2]:
                poss.append(permute(s,(0,2,1)))
            if s[1] != s[2] or s[1] != s[0]:
                poss.append(permute(s,(1,2,0)))
                poss.append(permute(s,(2,0,1)))
            poss2.append(s)
            if s[0] != s[1]:
                poss2.append(permute(s,(1,0,2)))
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
