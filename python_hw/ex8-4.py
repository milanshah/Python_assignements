class MyError(exception):
    pass

def oops():
    raise MyError, 'hello'

def f():
    try:
        oops()
    except (IndexError, MyError) as e:
        print(e.args)  #args is the 'hello'
