# Strings

# Single_quotes = 'Look! single quotes' # Single quotes also used to quote people and apostrophes
# Double_quotes = "Look! double quotes"
# print(Single_quotes)
# print(Double_quotes)
#
# # string_failure = '! said 'Wow!'
#
# escape_example = 'I said \'Wow\'' # Escape character \ lets you ues single quotes in a string
# print(escape_example)
# quote_in_quote = 'I said "Wow!"'
# print(quote_in_quote)
# reversed_quote = "I said 'Wow!'" # Easiest to visualise, can also easily use apostrophes
# print(reversed_quote)

# String slicing

# Everything in code starts with 0 not 1
# H e l l o   w o r l d !
# 0 1 2 3 4 5 6 7 8 9 10 11

# Hw = "Hello world!"
# print(Hw[7:]) # orld!
# print (Hw[-5:]) # orld!
# print(Hw[:5]) # Hello
# print(Hw[0:5]) # Hello

# String methods

# strip()

# white_space = "lots's of space at the end                        "
# print(len(white_space)) # 50
# print(len(white_space.strip())) # 26
#
# example_text = "Here's some text with lot's of text"
#
# # Count a substring within a string
# print(example_text.count("text")) #2
#
# # Make everything lower case
#
# print(example_text.lower())
#
# # Make everything upper case
# print(example_text.upper())
#
#
# # Capitalise things
# print(example_text.capitalize())
#
# # Replace characters/text
# print(example_text.replace("with" , ","))
#
# # Concatenation
#
# a = "here "
# b = "more "
# c = "much more"
#
# print(a + b + c)
#
# # Casting
#
# x = 2
# y = 5.4
# z = " there's a number 25.4 unless we put a space!"
#
# print(str(x) + str(y) + z)
#
# # string to numeric
#
# int_string = "6"
#
# print(float(int_string))
# print(type(int(int_string)))

# F-strings - formats automatically so different data types can be used in a string

# name = "Lassie"
# years = 7
# height_cm = 60.2
#
# print(f"{name} is {years} years old and {height_cm} cm tall")

# f-strings allow us to use methods/evaluations

name = "Snoopy"
years = 52

print(f"{name.upper()} is {years * 7} years old in dog years")

# F-strings to specify precision in rounding and decimals

pi = 3.14159265359

print(f"Pi to 3 decimal places: {pi:.3f}") # Pi to 3 decimal place
print(f"Pi to 5 decimal places: {pi:.5f}") # Pi to 5 decimal place

score = 16
max_score = 26

print(f"You scored {score/max_score}") # 0.6153846153846154
print(f"You scored {score/max_score:%}")  #61.538462%
print(f"You scored {score/max_score:.0%}") #62%