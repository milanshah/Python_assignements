def oops():
    raise IndexError, 'hello'

def f():
    try:
        oops()
    except IndexError:
        print('caught IndexError exception')

def oops():
    raise KeyError, 'hello'
