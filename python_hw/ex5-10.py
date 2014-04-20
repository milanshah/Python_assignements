def quicksort(L):
    if len(L) > l:
        less = [x for x in L if x < L[0]]
        med = [x for x in L if x == L[0]]
        more = [x for x in L if x > L[0]]
        return quicksort(less) + med + quicksort(more)
    else:
        return L
                

def insertion_sort(mylist):
    for j in range(1,len(mylist)):
        key = mylist[j]
        i=j
        while i > 0 and mylist[i-1] > key:
            mylist[i] = mylist[i-1]
            i -=1
            mylist[i] = key



"""
draft from classroom

"""


