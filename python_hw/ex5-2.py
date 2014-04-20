def countPages(n):
    print(sum([str(i).count('1') for i in range(n+1)]))


countPages(200)
countPages(100)
countPages(11)

"""
eg.

range 1 to 11:      0  1  2  3   4  5  6  7  8  9  10 11
new list:           0  1  0  0   0  0  0  0  0  0  1  2

then add the new list [0 1 ... 1 2]

"""
