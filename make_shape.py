from core import Shape, three_parts

s = Shape([[1,0],[0,1]])
t = Shape([[0,1],[1,0]])

print s
print t
print s == t

poss_3 = []
count = 0
for s in three_parts(3):
    poss_3.append(s)
print poss_3
