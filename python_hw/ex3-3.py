def fix_start(s):
    s1=''
    s1 = s[0] + s[1:].replace(s[0],'*')
    return s1
    
print(fix_start('babble'))


"""
return s[0] + s[1:].replace(s[0],'*')
"""
