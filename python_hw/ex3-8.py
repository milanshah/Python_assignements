def double_char(s1):
    s2 = ''
    for item in s1:
        s2 = s2 + (item * 2)
    return(s2)



a = 'The'
print(double_char(a))
a = 'AAbb'
print(double_char(a))
a = 'Hi-There'
print(double_char(a))
