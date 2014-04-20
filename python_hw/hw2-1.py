list1 = [1,4,2,2,3,1,2,3]

def remove_duplicates(input_list):
    """All duplicate elements have been reduced to a single element"""
    i = 0
    for item in input_list:
        #the previous one will be checked again.
        i = input_list.index(item)
        while i < len(input_list):
            print('item is: ', item,' ;i is: ', i,' ;len is: ', len(input_list))
            #Without (len(input_list)), error pops up in (item == input_list[i+1])
            if i < (len(input_list) - 1):
                if item == input_list[i+1]:
                    #if finding the same value, delete that value
                    del input_list[i+1]
            print('              i is: ',i,' ,and new list is: ',input_list)
            i = i + 1
    return input_list



new_list = remove_duplicates(list1)
print('the new list is: ',new_list)
