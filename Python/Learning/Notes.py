# // - quotient - how many times x goes into y
# % - modulo - remainder of the division
# ** to the power of
# \ escape character - can be used to include a quote in a string eg.
print("Today\'s a good day")
# \n - new line
# \t - tab in
# """ - print new lines
# Concatenation - adding two strings together
# x = y 'x' is the variable, '=' is the assignment operator, 'y' is the value
# Variables can contain letters, numbers and underscores
# del - removes a variable
# input() prompts user for input
# To produce a prompt message include a string to input(), eg.
name = input("Enter your name: ")
print(name)
# To change the input from a string use the relevant function, eg.
age = int(input())
height = float(input())
print(age) + (height)
# To use a number in a string concatenation use the str() function, eg.
print("Their age is " + str(age))
# In-Place Operators +=, -=, *=, /=, //=, %=, **=,
# Booleans only have 2 values - True & False

# To create a list with a range of numbers, eg.
numbers = list(range(10))
print(numbers)
# You can also specify the interval by adding in a 3rd, eg.
numbers = list(range(5, 20, 2))
print(numbers)
# You can use ranges in for loops, without converting them into lists, eg.
for i in range(5):
    print("hello!")
# List slices produce part of a list containing all the values between the indices, eg.
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[2:6])
print(squares[:5])
print(squares[5:])
# Using [::-1] as a slice is a common and idiomatic way to reverse a list, eg.
nums = [5, 42, 7, 1, 0]
res = nums[::-1]
print(res) 
# len() produces the number of items in a list
# append() is used to add an item to the end of the list
# Strings have a format() function, which enables values to be embedded in it,
# using placeholders
# join() joins a list of strings with another string as a separator.
# replace() replaces one substring in a string with another
# lower() and upper() change the case of a string to lowercase and uppercase
# functions can take arguments, which can be used to generate the function output, eg.
def exclamation(word):
   print(word + "!")
exclamation("spam")
# Once you return a value from a function, it immediately stops being executed.
# Any code placed after the return statement won’t be executed.
# A function can only return once, thus, if you need to return multiple values, you can use a list.
# Docstrings (documentation strings) are similar to comments but as more specific and have a different syntax.
# They’re created by putting a multiline string containing an explanation of the function below the function's
# first line, eg.
def shout(word):
  """
  Print a word with an
  exclamation mark following it.
  """
  print(word + "!")
shout("spam")
