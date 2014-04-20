def prettify(f):
    def wf(*args):
        print('#########')
        print('$$$$$$$$$$$$')
        f(*args)
        print('$$$$$$$$$$$$')
        print('#########')
    return wf

@prettify
def print_somtthing(s):
    print(s)



print_something("hello")
    
