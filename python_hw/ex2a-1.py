def linear_merge(list1, list2):
    k = (list1 + list2)
    new_list = []
    l = len(k)
    i = 1
    print('the list is: ', k)
    while i <= l:
        j = min(k)
        k.remove(j)
        new_list.append(j)
        print('index is: ',i,'; value is: ',j, ' new list is: ',new_list)
        i = i + 1

    print('the sorted list is: ',new_list)

    
list1 = [1,2,6]
list2 = [0,3,4]
linear_merge(list1, list2)
