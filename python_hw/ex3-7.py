def end_other(s1,s2):
    s1 = s1.lower()
    s2 = s2.lower()
    return(s1.endswith(s2[-1]))



a = 'Hiabc'
b = 'abc'
print(end_other(a,b))
a = 'Abc'
b = 'HiaBc'
print(end_other(a,b))
a = 'abc'
b = 'abXabc'
print(end_other(a,b))

"""
return a.endwith(b) or b.endwith(a)
"""
