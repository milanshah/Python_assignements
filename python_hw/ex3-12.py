def count_code(s):
    count = 0
    s1 = s.split('co')
    for item in s1:
        if len(item) >= 2:
            if item [1] == 'e':
                count = count + 1
    #Above lines give an error if the 2nd letter of the original string is 'e'.
    #Here is the checking for this error:
    if s[1] == 'e':
        count = count - 1
    return(count)

    
a = 'aaacodebbb'
print(count_code(a))
a = 'codexxcode'
print(count_code(a))
a = 'cozexxcope'
print(count_code(a))
a = 'aeacodebbb'
print(count_code(a))


"""
s=s.lower()
c=0
while len(s) >= 4:
    i=s.fin('co')
    if s[i]+3 == 'e':
        c=c+1
    s=s[(i+4):]
return c

"""
