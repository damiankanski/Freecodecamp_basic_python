# Dictionaries
band = {
    "vocals": "Plant",
    "guitar": "Page"
}

band2 = dict(vocals="Plant", guitar="Page")

print(band)
print(band2)
print(type(band2))
print(len(band2))

# Access items
print(band["vocals"])
print(band.get("guitar"))

#list all keys
print(band.keys())

#list of values
print(band.values())

# list of key/value as pairs of tuple
print(band.items())

#veryfi keys

print("guitar" in band)
print("skso" in band)

# Change values
band["vocals"] = "Coverdale"
band.update(({"bass": "JPJ"}))

print(band)

# Remove items
print(band.pop("bass"))
print(band)

band["drums"] = "Bonham"
print(band)

print(band.popitem())
print(band)

# Delete abd clear

band2.clear()
print(band2)

del band2

# Copy dictionaries

band2 = band.copy()
band2["drums"] = "Dave"
print(band)
print(band2)


# Nested dictionaries

member1 = {
    "name": "Page",
    "instrument": "vocals"
}
member2 = {
    "name": "Plant",
    "instrument": "guitar"
}
band = {
    "member1": member1,
    "member2": member2
}

print(band)
print(band["member1"]["name"])

# Sets

nums = {1, 2, 3, 4}

nums2 = set((1,2,3,4))
print(nums)
print(nums2)

# No duplicate allowed (pomija powtarzajace sie wartosci)

nums = {1,2,2,2,3,3,4,4,4}
print(nums)

# True is 1 and False is 0.

nums = {1, True, False, 2, 0}
print(nums)

# Add new element to a set
nums.add(8)
print(nums)

# Add elements from set to another set

morenums = {5,6,7}
nums.update(morenums)
print(nums)

#marge two sets to create a new set
one = {1,2,3}
two = {5,6,7}

mynewset = one.union(two)
print(mynewset)

# Keep only the duplicates
one = {1,2,3}
two = {2,3,4}

one.intersection_update(two)
print(one)

# Keep everything except duplicates
one = {1,2,3}
two = {2,3,4}

one.symmetric_difference_update(two)
print(one)



