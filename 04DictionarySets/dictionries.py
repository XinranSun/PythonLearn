# Dictionaries
band = {
    "vocals": "Plant",
    "guitar": "Page",
    "carbohydrates": "keyi"
}

brand2 = dict(vocals="Plant", guitar="heiha")
print(brand2.keys())
print(brand2.values())
print(brand2.items())
print("gui" in brand2)
brand2["guitar"] = "abcv"
print(brand2)

brand2.update({"guitar": "data"})
print(brand2)

brand2.pop("guitar")
print(brand2)
print("----")
print(brand2.popitem())

brand2["Plant"] = "Plant"
print(brand2)
del brand2['Plant']

print("---")
print(brand2)

# Copy dictionaries
print(" bad copy just reference!")
band2 = band
print(band)
print(band2)
band2["Plant"] = "Plant"
print(band)
print(band2)

print("good copy .copy()")
band2 = band.copy()
band2["h"] = "Plant"
print(band)
print(band2)

print("good copy dict()")
band2 = dict(band)
band2["hads"] = "Plant"
print(band)
print(band2)

# Nested dictionaries
print("Nested Dictionary")
member1 = {
    "first_name": "John",
    "last_name": "wo"
}
menber2 = {
    "first_name": "John",
    "last_name": "woasd"
}

ha = {
    "first_name": member1,
    "last_name": menber2
}
print(ha["first_name"]["first_name"])

# Sets No duplicate
first = [1, 2, 23]
second = (1, 2, 3, 4)
third = {"ha": "123"}
four = {1, 2, 3, 4}
print(type(first), type(second), type(third), type(four))
# 按序排列, 1=True ,0=False delete重复
nums = {1, True}
nums1 = {1, False}
nums2 = {1, 10, True, False}
print(nums)
print(nums1)
print(nums2)
# update = list ,tuple, dicti..
morenums = {1, 6, 7}
nums2.update(morenums)
print(nums2)
# merge two sets to create a new set
one = {1, 2, 3}
two = {2, 3, 4}
mynewset = one.union(two)
print(mynewset)

# keep only the duplicates
one.intersection_update(two)
print(one)
one = {1, 2, 3}
# keep everything except the duplicates
one.symmetric_difference_update(two)
print(one)
one.n
