list1 = [1,2,2,3,3,4,5,6,6]

def remove_adjacent(nums):
    i = 0
    for item in nums:
        i = nums.index(item)
        while i < (len(nums)-1):
            if nums[i] == nums[i+1]:
                del nums[i+1]
            i = i + 1
            #print(nums)
    return nums


print(remove_adjacent(list1))




"""
def remove_adj(nums):
    new_nums[]
        for n in nums:
            if n!= new_nums[-1]:
            new_nums.append(n)
    return new_nums

"""
