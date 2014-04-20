#list1 = [3,88,44,2,88,1,3,2]

def remove_elements(lst):
    """Remove Max, Min value and number 3 value"""
    max_value = max(lst)
    min_value = min(lst)
    for item in lst:
        if item == max_value:
            lst.remove(item)
    for item in lst:
        if item == min_value:
            lst.remove(item)
    for item in lst:
        if item == 3:
            lst.remove(item)
    return lst



def str_to_lst(tmp):
    """Change the string to int"""
    str_lst = tmp.split()
    i = 0
    for item in str_lst:
        str_lst[i] = int(item)
        i = i + 1
    return str_lst
    print('the int list =',str_lst)

    

str1 = input("enter a list with a space between each one: ")
list1 = str_to_lst(str1)
print(remove_elements(list1))

"""
better to create a new list, so don't use the remove.

new+nums=[]
for n in nums:
    for n != max and n != min and n != 3:
         new_nums.append(n)
return new_nums
"""




