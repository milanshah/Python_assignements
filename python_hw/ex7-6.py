def dirsearch():
    w = input('please enter search string')
    cwd = os.getcwd()
    lfiles == os.listdir(cwd)
    for file in lfiles:
        if os.spliter(file)[1] == 'txt':
            f.open(file)
            for l in f:
                c += 1
                if w in l:
                    print(f,c,l)
            f.close()
            
    
"""

"""



