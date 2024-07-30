from functools import reduce

squared = lambda x: x ** 2
addTwo = lambda num: num + 2

print(squared(2))
print(addTwo(5))


# sum = lambda a, b:  a + b
# print(sum(1, 2))


# funcBuild : def-return lambda....
def funcBuilder(x):
    return lambda n: n + x


addTen = funcBuilder(10)
addTwenty = funcBuilder(20)
print(addTen(5))
print(addTwenty(5))
print("---------")
print("higher func")
numbers = [1, 2, 3, 5, 7, 2, 3]
squared = map(lambda num: num * num, numbers)
print((f"squared numbers : {list(squared)}"))

odd_numbs = filter(lambda num: num % 2 != 0, numbers)
print(f"odd numbers: {list(odd_numbs)}")

reduced = reduce(lambda acc, curr: acc + curr, numbers, 10)
print(f"reduced: {reduced}")
print(f"sum : {sum(numbers, 10)}")

names = ['Dave Gray', 'Sara Ito', 'John Jacob Jingleheimerschmidt']

char_count = reduce(lambda acc, curr: acc + len(curr), names, 0)

print(char_count)
