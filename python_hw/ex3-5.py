def match_ends(words):
    i = 0
    for item in words:
        if len(item) >=2 and item[0] == item[-1]:
            i = i + 1
    return i


w = ['a', 'hello', 'helloh', 'abcda', 'qqqqq']
print(match_ends(w))
