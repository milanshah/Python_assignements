def mix_up(a,b):
    a1 = b[:2] + a[2:]
    b1 = a[:2] + b[2:]
    return(a1 + ' ' + b1)

"" refectoring the code ""
s1 = 'dog'
s2 = 'dinner'
print(mix_up(s1,s2))

"""
return b[:2] + a[2:] + ' ' + a[:2] + b[2:]
"""
