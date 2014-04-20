def reverseLookup(d, num):
    l = []
    for key, value in d.items():
        if num == value:
            l.append(key)
    print(sorted(l))

d1 = {'a':1, 'b':2, 'c':2}
reverseLookup(d1, 1)
reverseLookup(d1, 2)
reverseLookup(d1, 3)


"""
l.sort()
return l

or
l = []
for i in d.keys():
    if v == d[i]:
        l.append(i)
l.sort()
return


"""
