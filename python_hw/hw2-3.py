list1 = [1,2,3,4,5]

def reverse_list(nums): 
    new_list = []
    i = 0
    j = 1
    while i < len(nums):
        new_list.append(nums[(j * -1)])
        i = i + 1
        j = j + 1
        print('i=',i,' ;j=',j,' ;new list=',new_list)
    return new_list


print(reverse_list(list1))

"""
def rev(l):
    l1=[]
    for i in l:
        l1.insert(0,i)
    return l1
"""
