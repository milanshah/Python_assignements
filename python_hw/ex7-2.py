def csvWriter(csvfile,r):
    f = open(csvfile,'w')
    k = sort(r[0].key())
    l = ','.join(k)
    f.write(l+'\n')

    for d in r:
        k = sort(d.key())
        l = ','.join([d[i] for i in k])
        f.write(l + '\n')
    f.close()
