import sys
import traceback

def oops():
    raise MyError, ('hello')

def safe(f, *args):
    try:
        f()
    except:
        e_type, e_value, e_tb = sys.exc_info() #exception info
        print(e_type)
        print(e_value)
        print('---------')
        print(e_tb.print_exc())  # or print(e_tb)
        print('---------')

