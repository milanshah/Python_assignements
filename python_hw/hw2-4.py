list1 = [3,8,44,2,1,3,2]

def front_3(lst):
    new_list = []
    for item in lst:
        if 3 == item:
            lst.remove(item)
            new_list.append(item)
    lst.sort()
    for item in lst:
        new_list.append(item)
    #print('lst=',lst,' ;new list=',new_list)
    return new_list


print(front_3(list1))
