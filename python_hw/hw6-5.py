def convert_time(s):
    h = int(s /3600)
    m = int((s % 3600)/60)
    s1 = s % 60

    out=''    #output
    if h:
        out = out + str(h) + ' hr'
    if m:
        out = out + str(m) + ' min'
    if s:
        out = out + str(s1) + ' sec'
    return out
