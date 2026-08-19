#Day 1 - Introduction to Python

### print ()
This is used to print the output

### Arithmetic operators
+ add
- subtract
* multipy
/ divide
% modulus - returns the remainder of a division operation between 2 numbers 
// floor division - divides 2 numbers and rounds the result down to the nearest whole number

when using "+" with strings, it will join the text
print("42" + "8") means "42" + "8", resulting in 428

#What I Learned

1. What is a data type?
A data type specifies what kind of data a value represents and how Python should treat that data.

2. What is the difference between an int, float, and string?
Single Value Data Type
String (str): textual data enclosed in single, double, or triple quotes
Integer (int): positive or negative whole numbers without a decimal point
Float: real numbers containing one or more decimal points
Boolean (bool): logical values represnting truth states
 
3. What is the difference between a list, tuple, set, and dictionary?
List: [] ordered, mutable sequences that allow duplicate items.
Set: {} unordered collections of unique items with no duplicates allowed
Tuple: () ordered, immutable sequences used to store fixed data sets
Dictionary: {"x":"x"} unordered, mutable collections of key-value pairs where keys mustbe unique.

4. What does type() do?
This will print what the data type is instead of the actual output.

5. Why did "10" * 3 produce 101010 instead of 30?
When "10" is enclosed in quotes, Python treats it as a string rather than an integer.
Therefore, "10" * 3 repeats the string three times, producing "101010" rather than 30.

6. Why did Python give you a NameError when you initially wrote:
   name: Gina
Gave me this error becuase I wrote both key and values without quotations.
Python was interpreting them as variable names rather than strings. By putting them in quotation marks, I told Python they were text.
