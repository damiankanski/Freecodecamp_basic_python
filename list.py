users = ["Dave", "John", "Sara"]

data = ["Dave", 42, True]

emptylist = []

print("Dave" in emptylist)

print(users[0])
print(users[-1])
print(users.index("Sara"))
print(users[0:2])

print(len(data))

#dodanie na koneic listy
users.append("Elsa")
print(users)

# Dodanie na koniec listy warotsci koniedcnie musi byc to lista
users += ["Jason"]

print(users)

#rozszerzenie listy o dwie wartosci lub wiecej
users.extend(["Robert", "Jimy"])
print(users)
print("\n\n")

# users.extend(data)
# print(users)

#Dodanie warotsic w konkretne m iejsce listy
users.insert(0, "Bob")
print(users)

#wkleje wartosci pomiedzy w  liscie
users[2:2] = ["Eddie", "Alex"]
print(users)

#podmienianie wartosci
users[1:3] = ["Robert", "JPJ"]

#usuwanie wartosci z listy

users.remove("Bob")
print(users)

#ususwanie ostatniej wartosici z listy momzna przypisac do zmiennnej
print(users.pop())

#usuwanie po index
del users[0]

#ususneniecie calkowite listy
# del data
# print(data)

#czyscienei wartosci list

data.clear()
print(data)

#sortowanie ASC

users.sort()
print(users)

#sortowanie od np wartosci z malych liter

users.sort(key=str.lower)
print(users)

# odwrocenie listy
nums = [4,42,78,1,5]
nums.reverse()
print(nums)

#sortowanie od DESC bez zmiany listy
print(sorted(nums, reverse=True))


#kopiowanie
numscopy = nums.copy()
mynums = list(nums)
mycopu = nums[:]
print(numscopy)

#Tuples niezmienne listy czyli krotki

mytuple = tuple(("Dave", 42, True))
print(mytuple)

