def primeNumbers(n):
    if n==1:
        return[]
    else:
        l=[2]
        for i in range(3,n+1,2):
            for j in range(2,1):
                if i%j==0:
                    break
            else:
                l.append(i)
        return l


primeNumbers(5

"""
draft from classroom

"""


