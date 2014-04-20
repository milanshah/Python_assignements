def str_reverse(s):
    i = 1
    s1 = ''
    for item in s:
        s1 = s1 + s[i * -1]
        i = i + 1
    return(s1)
        
a = 'hello'
print(str_reverse(a))

"""
-- create a new string
-- add each letter in front of the previous one

def str_rev(s):
    ns = ''
    for item in s:
        ns = item + ns
    return ns


or
return s[::-1] (slicing in list)

eg:
s = helloword
   012345  
s[0:5:2] will be "hlo"
"""
