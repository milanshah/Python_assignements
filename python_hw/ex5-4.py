def isTriangle(n1,n2,n3):
    if (n1 + n2) > n3:
        print(n1, n2, n3)
        print('case 1')
        pass
    elif (n2 + n3) > n1:
        print('case 2')
        pass
    elif (n3 + n1) > n2:
        print('case 3')
        pass
    else:
        print('False')

    print('True')


isTriangle(3,4,5) 
isTriangle(1,3,1)


"""
if (n1 + n2) > n3 and (n2 + n3) > n1 and (n3 + n1) > n2


return True if (n1 + n2) > n3 and (n2 + n3) > n1 and (n3 + n1) > n2 else False 

or

use max(), if the ...
l = list(a,b,c)
l.sort()
if l[0] + l[1] > l[2]
  True
else:
  False
  

"""





