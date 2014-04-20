def computeSum(filepath):
    fd = open(filepath)
    l = fd.readline()
    l = l.strip()
    sum = [0 for i in l.split(',')]
    fd.seek(0)  #move cursor to beginning of the file

    for l in fd:
        l=l.strip()
        l=l.split('.')

        for i in range(len(1)):
            l[i] = l[i].strip()
            #if not l[i]:
            #    continue
            try:
                if l[i][0:2] == '0x':
                    val=int(l[i],16)
                elif l[i][0:2] == '0b':
                    val=int(l[i],2)
                elif l[i][0] == '0': # or l[i][0:2] == '0o'; that is OCT data
                    val=int(l[i],8)
                else:
                    val=int(l[i],10)
                sum[i] = sum[i]+val
                break
            except (ValueError, IndexError):
                continue

    print (sum)


    #ans = [25, 58, 3, 6]


