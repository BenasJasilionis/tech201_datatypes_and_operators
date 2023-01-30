# Boolean

# True or False

# a = True
# b = False
#
# print(a == b) # False
# print(a != b) # True
# print(a >= b) # True (true considered greater than false)
# print(b <= False) # True

# print(True and False) # False
# print(False and True) # False
# print(False or True) # True

# Booleans are useful for quickly checking the state of something.
# The other area Booleans are really useful are validating data types

# Booleans with Data types

# hi = "Hello world!"
#
# print(hi.isalpha()) # False - isalpha checks if everything is also numeric ( no spaces or punctuation)
# print(hi.islower()) #False
# print(hi.isupper()) #False
# print(hi.endswith(" world!")) #True
# print(hi.startswith("Hello")) # True

# x = 0
# y = 10
# z = -15
# print(bool(x)) # False - 0 is considered False
# print(bool(y)) # True
# print(bool(z)) # True

# None


# None == Null in a lot of other languages

print(bool(None)) # False#

x = None

print(x == False) # False
print(x == True) # False   None is in its own category cant be true or false

# Checking if a variable is None

print(x == None) # direct comparison - more complex situations can make this suboptimal.
print(x is None) # Best practice for checking if something is None

print(type(x)) # <class 'NoneType'>


