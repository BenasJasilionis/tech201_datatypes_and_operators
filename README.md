# tech201_datatypes_and_operators
tech201_datatypes_and_operators
# Data Types

### Arithmetic operators

* +: add
* -: subtract
* *: multiply
* /: divide


### Comparison operators
* .> : greater than
* <  : less than
* == : equal to
* != : not equal to
*  .>=: greater or equal to
* <= : less than or equal too

## Numeric data types
* Ints - Whole numbers
* Floats - Numbers with decimals
* Longs- Long numbers (has to pass a thresh hold)
* Complex numbers

### Extra notes about numerical data
* Floats and ints can be multiplied and added due to both being numerical
* There is no limit to python decimal points, but python will round up
* For instance 1/3 * 3 will output 1.0

## Text data types
* String - Text of any type

### Quoting strings
* Strings can be quoted using "" or '' quotation marks
* Best practice is to use "" so that '' can be used as speech marks or apostrophes without error
* For example : `print("He said: 'Hello there'")` would correctly print the quotation marks.
* Escape characters can also be used to correctly format quotes:
* `print("He said : \"Hello there\"")` would also correctly print
* The backwards slash `\` symbol is an escape character which allows the same quote types to be used

### String slicing
Every data set in coding start at index 0, which is important to know when slicing as strings can be sliced by specifying indexes. This can be visualised below:
* H = 0 = -12
* e = 1 = -11
* l = 2 = -10
* l = 3 = -9
* o = 4 = -8
*   = 5 = -7
* w = 6 = -6
* o = 7 = -5
* r = 8 = -4
* l = 9 = -3
* d = 10 = -2
* ! = 11 = -1

Note that empty space (known as white space) also counts as an index and that negative indexing starts from -1

* Strings are sliced with the following syntax -> `variable[index of start(inclusive):index of end(non inclusive)`
* Below are some examples:

````
 Hw = "Hello world!"
 print(Hw[7:]) # orld!
 print (Hw[-5:]) # orld!
 print(Hw[:5]) # Hello
 print(Hw[0:5]) # Hello
````

### String methods - .strip()
* The last white space in strings can be removed with the `variable.stip()` command
* Arguments can be passed into `.strip()` to strip a character rather than white space
* We can see this in action by using the `len()` command which tells us how many indexes are in a data set:

````
white_space = "lots's of space at the end                        "
print(len(white_space)) # 50 (
print(len(white_space.strip())) # 26
````

### String methods- .count()
* Objects within a data set can be counted using `variable.count("character to be counted")`:
```` 
example_text = "Here's some text with lot's of text"
print(example_text.count("text")) #2
````
### Make everything lower case - .lower()
* A string can be lover case by using `variable.lower()`:
````
print(example_text.lower()) # here's some text with lot's of text
````
### Make everything upper case - .upper
````
print(example_text.upper()) # HERE'S SOME TEXT WITH LOT'S OF TEXT
````
### Capitalise things - .capitalize()
* The first character of a string can be capitalised by using `variable.capitalize()`:
````
print(example_text.capitalize()) # Here's some text with lot's of text
````
### Replace characters/text - .replace()
* Characters/text can be replaced using `variable.replace("old character", "new character")`
````
print(example_text.replace("with" , ",")) # Here's some text , lot's of text
````

### Concatenation
* Strings can be concatenated using the `+` operator
* Only strings of the same data type can be concatenated, i.e. strings with strings and numerical data with numetical data
````
a = "here "
b = "more "
c = "much more"
print(a + b + c)  # here more much more
````
* Note the spaces left at the end of variables `a` and `b`, without those spaces the string would instead concatenate like this: `heremoremuchmore`

### Casting
* The datatype of some variables can be changed, so that they can be concatenated:
* `str(var)` produces a variable
* `int(var)` produces an integer
* `float(var)` produces a float

This can be visualised below:
````
x = 2
y = 5.4
z = " there's a number 25.4 unless we put a space!"
print(str(x) + str(y) + z) # 25.4 there's a number unless we put a space!
````
* The same conversions can be made into floats and from strings into ints:
````
int_string = "6"
print(float(int_string)) # 6.0
print(type(int(int_string))) # 6
````
### F-strings - 
F-strings format automatically so different data types can be used in a string like ints, strings, lists, etc.
* The syntax for f strings is `print(f"string string {variable} string text {variable}`
````
name = "Lassie"
years = 7
height_cm = 60.2
print(f"{name} is {years} years old and {height_cm} cm tall") # Lassie is 7 years old and 60.2 cm tall
````
* F-strings are very useful because they allow for methods/evaluations to be used on the variables within the string:
````
name = "Snoopy"
years = 52
print(f"{name.upper()} is {years * 7} years old in dog years") #SNOOPY is 364 years old in dog years
````
* F-strings can also be used to specify precision in rounding and decimals
* Within the f-string the syntax looks like this `{variable:.<number of places to be rounded>f`

Example below:
````
pi = 3.14159265359
print(f"Pi to 3 decimal places: {pi:.3f}") # Pi to 3 decimal place
print(f"Pi to 5 decimal places: {pi:.5f}") # Pi to 5 decimal place
````
# F-strings and percentages
As mentioned previously, f-strings can be used for calculations, but they can also be used for percentages:
* The syntax for percentages within the f-string is: `{variable:<decimal points>%}`
````
score = 16
max_score = 26
print(f"You scored {score/max_score}") # 0.6153846153846154
print(f"You scored {score/max_score:%}")  #61.538462%
print(f"You scored {score/max_score:.0%}") #62%
````
# Boolean
* Booleans are concerned with evaluating whether something is `True` or `False`
* Note how both `True` and `False` are capitalized

Below are some common comparisons which will help establish how booleans function:
````
a = True
b = False

print(a == b) # False
print(a != b) # True
print(a >= b) # True (true considered greater than false)
print(b <= False) # True

print(True and False) # False
print(False and True) # False
print(False or True) # True
````
* Booleans are useful for quickly checking the state of something.
* The other area Booleans are really useful are validating data types

### Booleans with data types
Booleans can be used to check whether data meets certain conditions, returning `True` if so and `False` if it doesn't:
````
hi = "Hello world!"

print(hi.isalpha()) # False - isalpha checks if everything is also numeric ( no spaces or punctuation)
print(hi.islower()) #False
print(hi.isupper()) #False
print(hi.endswith(" world!")) #True
print(hi.startswith("Hello")) # True
````
### Booleans and numbers
Below are some examples that show how booleans interact with numbers using the `bool()` command to determine whether a number meets the criteria for `True` or `False`:
````
x = 0
y = 10
c = 1.5
z = -15
print(bool(x)) # False - 0 is considered False
print(bool(y)) # True
print(bool(c)) # Floats are True
print(bool(z)) # True - Negative values are still True
````

# None
`None` is known as `Null` in a lot of other languages ,it is often used as a placeholder for variables which have yet to be defined, so that the code can run without error.
* Note how `None` is also capitalised
````
x = None

print(x == False) # False
print(x == True) # False
````
* `None` is in its own category, therefore it always come up as `False` when testing with a `bool()` command:
`print(type(x)) # <class 'NoneType'>`

# Checking if a variable is None
* Direct comparison - more complex situations can make this suboptimal:
`print(x == None)`

* Best practice for checking if something is None:
`print(x is None)`  
