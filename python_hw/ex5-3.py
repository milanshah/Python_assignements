def time24hr(n):
    s1 = ''
    s2 = ''
    s1 = n.split(':')[0]
    s2 = n.split(':')[1]
    s3 = s2[-2:]

    if s3 == 'am' and s1 == '12':
        s1 = '00'
    elif s3 == 'pm' and s1 < '12':
        s1 = str(int(s1) + 12 )

    s2 = s2[:2] + 'hr'
    print(s1 + s2)


time24hr('09:34am')
time24hr('12:15pm')
time24hr('02:15pm') 


"""
s2 = n.split(':')[1][0:2]
s3 = n.split(':')[1][2:]

or using 'endwith'



def time24hr (t)
  if t[-2:] == 'am':
    return{'00" if t.split(':')[0] -- '12' else t.split(':')[0] + (t.split(':')[1].replace('am','hr'))
    elif t[-2:] == 'pm'  
    
      


"""
