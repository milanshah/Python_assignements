import os

def read_file(filepath):
    f = open(filepath)
    lcount = 0
    wcount = 0
    ccount = 0
    for line in f:
        lcount = lcount + 1
        wcount = wcount + len(l.split())
        ccount = ccount + len(l)

    print(lcount)
    print(wcount)
    print(ccount)

    f.clsoe()

"""
import os

    if not os.path.exist(filepath):
"""
