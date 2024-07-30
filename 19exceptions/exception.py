

class JustNoCoolException(Exception):
    pass
x = 2
try:
    raise JustNoCoolException("JustNoCoolException")
    # print(x / 1)
except NameError:
    print("NameE123rror")
except ZeroDivisionError:
    print("ZeroDivisionError123")
except Exception as e:

    # dayin chulai
    print("Exception", e)
else:
    print("No exception")
finally:
    print("finally no errors")