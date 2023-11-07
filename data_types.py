import math
# String data type

# literal assignment
first = "Dave"
last = "Gray"

# print(type(first))
# print(type(first) == str)
# print(isinstance(first, str))


# constructor function
# pizza = str("Peperoni")
# print(type(pizza))
# print(type(pizza) == str)
# print(isinstance(pizza, str))

#Concatenation

fullname = first + " " + last
print(fullname)

fullname += '!'
print(fullname)

# Casting a number to a string
decade = str(1980)
print(decade )
print(type(decade))

statement = " I like music from the " + decade + "s"
print(statement)

# Multiple lines

multiline = """
Hey, how are you

I was just checking in.  
                                All good?
"""

print(multiline)

# Escaping special characters
sentence = "Cytat \"good news\"!\t\n\nWho say it ? "
print(sentence)

# String Methods

print(first.lower())
print(first.upper())
print(multiline.title())
print(multiline.replace("good", "fine"))


print(len(multiline))
print(len(multiline.strip()))
print(len(multiline.lstrip()))
print(len(multiline.rstrip()))

print("\n\n")

# Build a menu
title = "menu".upper()
print(title.center(20, "="))
print("Coffee".ljust(16, ".") + "$1".rjust(4))
print("Muffine".ljust(16, ".") + "$3".rjust(4))
print("Tea".ljust(16, ".") + "$2".rjust(4))

print("\n\n")
# String index values
print(first[1])
print(first[-1])
print(first[1:-1])
print(first[1:])

# some methods return boolean data
print(first.startswith("D"))
print(first.endswith("Z"))

# Boolean data type
myvalue = True
x = bool(False)
print(type(x))
print(isinstance(myvalue, bool))


# Numeric data types

## integer type
price = 100
best_price = int(80)
print(type(price))
print(isinstance(best_price, int))

## float type

gpa = 3.28
y = float(1.14)
print(type(gpa))
print(isinstance(y, float))

## complex
comp_values = 5+3j
print(type(comp_values))
print(comp_values.real)
print(comp_values.imag)

# Built-in functions for numbers

print(abs(gpa))
print(abs(gpa * -1))

print(round(gpa))
print(round(gpa,1))

print(math.pi)
print(math.sqrt(64))
print(math.ceil(gpa))
print(math.floor(gpa))

# Casting a string to a number

zipcode = "10001"
zip_value = int(zipcode)
print(type(zip_value))
