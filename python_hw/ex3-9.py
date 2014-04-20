def cat_dog(s1):
    if s1.count('cat') == s1.count('dog'):
        return('True')
    else:
        return('False')

a = 'catdog'
print(cat_dog(a))
a = 'catcat'
print(cat_dog(a))
a = '1cat1cadodog'
print(cat_dog(a))
