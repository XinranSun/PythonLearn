def hello_world():
    print("Hello")


# hello_world()

def hello_world1(num1, num2):
    print(num1 + num2)


# hello_world1(1,2)


def sum(num1=1, num2=2):
    if type(num1) is not int or type(num2) is not int:
        return
    return num1 + num2


total = sum(1)
print(total)


def multiple_items(*args):
    print(args)
    print(type(args))


multiple_items('Davb', "hslk")


def mult_name_items(**kwargs):
    print(kwargs)
    print(type(kwargs))


mult_name_items(first="Davb", last="sldjlks")
