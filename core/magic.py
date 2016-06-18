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

    def to_ascii(self):
        out = []
        for a in self.ls:
            ls = [b.to_ascii().split("\n") for b in a]
            out += ["".join([j[i] for j in ls]) for i in range(len(ls[0]))]
        return "\n".join(out)

def all_magic(n, m=None, path=None, output=False):
    if m is None:
        m = n
    if output:
        print "Running for shape", n, ",", m
    if path is not None:
        file = str(n)
        if m!=n:
            file += "-"+str(m)
        filename = path + "/" + file
        with open(filename,"w") as f:
            pass
    if output:
        print "Generating all threes..."
    all = All(n,m)
    if output:
        print "Threes generated."
        print "Looking for magic squares..."
    magics = []
    for r_number,r in enumerate(all):
        if output:
            print r_number, "/", len(all)
        cols = [[l for l in all if l[0]==r[i]] for i in range(3)]
        for c0 in cols[0]:
            for c1 in cols[1]:
                for c2 in cols[2]:
                    for i in [1,2]:
                        if not all.contains([c0[i],c1[i],c2[i]]):
                            break
                    else:
                        if all.contains([c0[0],c1[1],c2[2]]) and all.contains([c0[2],c1[1],c2[0]]):
                            m = Magic([c0,c1,c2])
                            if path is not None:
                                with open(filename,"a") as f:
                                    f.write(m.to_ascii())
                                    f.write("\n----------------------\n")
                            if output:
                                print m
                                print "---------------"
                            magics.append(m)
    if output:
        print "Done"
    return magics
