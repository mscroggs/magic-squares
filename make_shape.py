from core import all_magic,All
from IPython import embed


for i in range(1,5):
    
    print i
    m = all_magic(i)
    for a in m:
        print a
