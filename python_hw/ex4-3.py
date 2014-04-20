def invertDictionary(d):
    vl = []
    nkl = []
    vl = d.values()
    nkl = sorted(set(vl))


    nd = {}
    for num in nkl:
        l = []
        for key, value in d.items():
            if num == value:
                l.append(key)
        nd.setdefault(num,l)
    print(nd)


d1 = {'a':1, 'b':2, 'c':3, 'd':2}
invertDictionary(d1)
d1 = {'a':3, 'b':3, 'c':3}
invertDictionary(d1)
d1 = {'a':2, 'b':1, 'c':2, 'd':1}
invertDictionary(d1)


"""
*** much better code ***

def invert_d(d):
    inv_d = {}
    for k, v in d.items():
        if v in inv_d:
            inv_d[v].append(k)
            inv_d{v].sort()
        else:
            inv_d[v] = [k]

    return inv_d



"""
