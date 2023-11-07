# rekurencja czyli wywolywanie funckji przez dama siedze takei zapetlanie

# def add_one(num):
#     if ( num>= 9):
#         return num + 1
#
#     total = num + 1
#     print(total)
#
#     return add_one(total)
#
# add_one(0)

def add_one(num):
    if ( num>= 9):
        return num + 1

    total = num + 1
    print(total)

    return add_one(total)

newtotal = add_one(0)
print(newtotal)