def HR_database(idl, namel):
    d = {}

    i = 0
    while i < len(idl):
        d.setdefault(idl[i],namel[i])
        i = i + 1
    print(d)

    print('\nHere is the list you entered (sorted by name):')
    snl = sorted(namel)
    for n in snl:
        for key, value in d.items():
            if n == value:
                print(key, value)
    

    print('\nHere is the list you entered (sorted by employee number):')
    sidl = sorted(idl)
    for n in idl:
        for key, value in d.items():
            if n == key:
                print(key, value)


id_l = []
name_l = []
id = ''
name = ''
while id.lower() != 'end':
    id = input('Please enter employee ID (END for quit): ')
    if id.lower() != 'end':
        id_l.append(int(id.strip()))
        name = input('Please enter employee name: ')
        name_l.append(name.strip())

print(id_l)
print(name_l)
HR_database(id_l, name_l)



"""
#for testing:
l1 = [487, 533, 843, 964]
l2 = ['John Campbell', 'Jane Smith', 'Steve John', 'David Clark']
HR_database(l1, l2)
"""


"""
def hr_db():
d = {}
s = input('Please enter employee number and name, type END when done:')
while (s !='END'):
    num = int(s.split(none,1)[0])
    name = s.split(none,1)[1]
    d[num] = name      # for print num as the key
    d[name] = num      # for print name as the key
    s = input(...)     #repeat it again


keys = d.keys()        #or, keys = list(d.keys()); best practice
keys.sort()
print(' ...sorted by employee id')
for k in keys():
    print(k, d[k])



"""





