def add_one(num):
    if num >= 4:
        return num
    total = num + 1
    print(total)
    return add_one(total)



add_one(2)
print(add_one(7))
