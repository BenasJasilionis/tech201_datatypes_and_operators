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

### String methods - strip()
* The last white space in strings can be removed with the `stip()` command
* We can see this in action by using the `len()` command which tells us how many indexes are in a data set:

````
white_space = "lots's of space at the end                        "
print(len(white_space)) # 50 (
print(len(white_space.strip())) # 26
````

### String methods- count()
* This method will count how many times a given number/ sequence of letters appears in a data set
* 








## Boolean
* True or False

# Operators



# String methods