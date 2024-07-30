users = ['John', 'Smith', 'sdsd']
data = ['John', 'Smith', 'sdsd', 23]
emptyList = []
print("John" in data)
print("Smith" in data)
print("sdsd" in emptyList)

data[2:2] = ['sdsd', 'sadasd']
print(data)
data.pop()
print(data)

del users[0:2]
print(users)
data[2:2] = ['Aaasdsd', 'aasadasd']
data.sort()
print("----")
print(data)

data.sort(key=str.lower)
print(data)

nums = [23, 23, 4, 2, 24, 1, 5]
nums.reverse()
print("-----")
print(nums)

# nums.sort(reverse=True)
# print(nums)
print(sorted(nums, reverse=True))
numscopy = nums.copy()
mynums = list(nums)
mycopy = nums[:]
print('-------')
print(numscopy)
print(mynums)
print(mycopy)

#  tuple
tuple1 = (1, 2, 3, 2, 2, 2, 4, 6)
(num1, *num2, num3) = tuple1
print(num1)
print(num2)
print(num3)
print(tuple1.count(1))
print(tuple1.count(2))
