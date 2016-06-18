from core import all_magic,All
from IPython import embed


for i in range(1,5):
    with open("output/"+str(i),"w") as f:
        pass
    print i
    m = all_magic(i)
    for a in m:
        with open("output/"+str(i),"a") as f:
            f.write(unicode(a))
        print a
