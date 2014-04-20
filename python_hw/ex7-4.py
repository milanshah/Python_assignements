def inireader(inifile,dd):
    f = open('inifile')

    sechdr = ''
    d = {}
    for l in f:
        if l[0] == '[' and l[-1] == ']':
            if sechdr:
                dd[sechdr] = d
            sechdr = l[1:-1]
            dd[sechdr] = ''
        else:
            d[l.split('=')[0]) = l.split('=')[1]

    dd[sechdr] = d
    
"""

"""



