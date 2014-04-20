def everyother_reverse(s):
    i = 1
    s1 = ''
    while i <= len(s):
        s1 = s1 + s[i * -1]
        i = i + 2
    return(s1)
        
a = 'abcdefgh'
print(everyother_reverse(a))
a = 'abcdefg'
print(everyother_reverse(a))

"""
def eo.rev(s):
   return s[::-2}
"""
