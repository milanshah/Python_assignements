def convertDictionary(d):
    kl = []
    kl = d.keys()
    
    key = 0
    nl = []
    if len(d) != 0:
        max_num = max(kl)
        while key <= max_num:
            if key in d:
                nl.append(d.get(key))
            else:
                nl.append(0)
            key = key + 1 
    print(nl)
    
convertDictionary({0: 1, 3: 2, 7: 3, 12: 4}) 
convertDictionary({0: 1, 2: 1, 4: 2, 6: 1, 9: 1})
convertDictionary({})


"""
if d:
    m = max(list(d.keys()))
else:
    return []

l = [0] * (m + 1)           #create a list with all zero.
for i,j in d.items():
    l[i]=j
return l

"""
