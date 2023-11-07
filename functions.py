def hello_world():
    print("Hello world")


hello_world()


# definiujac funkcje musimy zadelkarowac w nawiasch jesj parametry
# natomiast kiedy podajem dane do wywolania funckji sa to argumenty

# def sum(num1, num2):
#     return num1 + num2
#
# total =sum(2 ,3)
# print(total)

# zwraca nam none gdy podamy argument nie bedacy int
# def sum(num1, num2):
#     if type(num1) is not int or type(num2) is not int:
#         return
#     return num1 + num2
#
# total =sum(2 ,3)
# print(total)

# podajemy defaultowa wartosc dla parametru num2, w momecie gdy nie podamu wartosci argumentu dla num2 bedzie to
# domyslnie 3
def sum(num1, num2=3):
    if type(num1) is not int or type(num2) is not int:
        return
    return num1 + num2

total =sum(2)
print(total)


# args uzywamy gdy nie zanmy ilosci paramtrow nalezy pamieatac ze zawsze zwroci nam to tupla
def multiple_name(*args):
    print(args)
    print(type(args))

multiple_name("Sara", "James")


# kwagrs keywaords podajemy key i valu zwracam nam funkcja dicta
def multi_name(**kwargs):
    print(kwargs)
    print(type(kwargs))

multi_name(firs="Sara", last="James")