def merge_lists(l1,l2):
    l3 = []
    for i,j in l1,l2:
        l3.append((i,j))
    return l3

    or return list(zip(l1,l2))  # convert to a list
