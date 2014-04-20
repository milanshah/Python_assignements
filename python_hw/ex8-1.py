def func():
    while True:
        try:
            a = input('please enter a')
            a = int(a)
            break
        except ValueError:
            pass
    while True:
        try:
            b = input('please enter b')
            a = int(b)
            break
        except ValueError:
            pass

    return a + b




"""
'continue' only use in loop
"""
