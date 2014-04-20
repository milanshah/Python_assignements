def sort_print(l):
    k = sorted(list(l.keys()))
    print('Dictionary: sorted by keys:')
    for i in k:
        print(i + ' ' + str(l.get(i)))
        
    v = sorted(list(l.values()))
    print('Dictionary: sorted by values:')
    for num in v:
        for key,value in l.items():
            if value == num:
                print(key + ' ' + str(num))
        

d = {'c':5,'b':2,'a':3}
sort_print(d)



"""
keys.sort()
for s in keys:
     print(x,d[x])

"""
