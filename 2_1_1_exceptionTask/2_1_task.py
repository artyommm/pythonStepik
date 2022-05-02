def foo():
    pass

try:
    foo()
except Exception as e:
    if isinstance(e, ArithmeticError):
        if isinstance(e, ZeroDivisionError):
            print("ZeroDivisionError")
        else:
            print("ArithmeticError")
    elif isinstance(e, AssertionError):
        print("AssertionError")
    else:
        print("Exception")

except BaseException:
    print("BaseException")