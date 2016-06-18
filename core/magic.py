from all import All

class Magic:
    def __init__(self, ls):
        self.ls = ls

    def __unicode__(self):
        out = []
        for a in self.ls:
            ls = [unicode(b).split("\n") for b in a]
            out += ["".join([j[i] for j in ls]) for i in range(len(ls[0]))]
        return "\n".join(out)

    def __str__(self):
        return unicode(self).encode('utf-8')


def all_magic(n,m=None):
    if m is None:
        m = n
    all = All(n,m)
    magics = []
    for r in all:
        cols = [[l for l in all if l[0]==r[i]] for i in range(3)]
        for c0 in cols[0]:
            for c1 in cols[1]:
                for c2 in cols[2]:
                    for i in [1,2]:
                        if not all.contains([c0[i],c1[i],c2[i]]):# and all.contains([c0[0],c1[1],c2[2]]) and all.contains([c0[2],c1[1],c2[0]]):
                            break
                    else:
                        print Magic([c0,c1,c2])
                        print ""
                        print ""
                        magics.append(Magic([c0,c1,c2]))
    return magics
