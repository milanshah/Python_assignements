def both_ends(s):
    if len(s) >= 2:
        f2 = s[:2]
        l2 = s[-2:]
        f2andl2 = f2 + l2
    else:
        f2andl2 = ''
    return(f2andl2)


print(both_ends('spring'))
print(both_ends('p'))

    
