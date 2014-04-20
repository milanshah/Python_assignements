def iniwriter(dd):
    f = open('input.ini','w')

    for k,v in dd.items():
        f.write("[" + k + "]\n")
        for sub_k, sub_v in v.items():
            f.write(sub_k + '=' + sub_v + '\n')
    f.close()




