def convertVector(d):
    key = 0
    nd = {}
    for value in d:
        if value != 0:
            nd.setdefault(key,value)
        key = key + 1
    print(nd)


convertVector([1, 0, 0, 2, 0, 0, 0, 3, 0, 0, 0, 0, 4])
convertVector([1, 0, 1 , 0, 2, 0, 1, 0, 0, 1, 0])
convertVector([0, 0, 0, 0, 0])


"""
for i in l:
    if i != 0:
       d[key] = i
    key = key + 1
return d
"""
