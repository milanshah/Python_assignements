def gethostname(ip):
    f = open('/etc/hosts')

    for l in f:
        l = (l.split('#')[0]).strip()
        if not l:
            continue
        i = l.split()[0]
        h = l.split()[1]
        if ip == i:
            f.close()
            return h
        f.close
        return 'unknown host'





"""
def gethostname(ip):
    f = open('hosts.txt', 'r')
    lines = f.readlines()
    f.close()

    flag = 0
    for l in lines:
        if (l.split()[0] == ip):
            print(l.split()[1])
            flag = 1
    if flag == 0:
        print('no found')


    
gethostname('127.0.0.1')
gethostname('192.168.2.253')
gethostname('192.168.2.254')
"""



