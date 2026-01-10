# this is the firs ever code in python.
print("Hello world")

# using inbuild function
print("this is my first day larning python.") 

# return value
# a value is return by a function and to store within a variable
message = print("this is the return value of print function.")

# printing the return value with print function.
print(message)

# variable to store values returned by a function or by user specified
name = "Ripon"   # name is variable and "Ripon" is value
age = 22   # age is variable and 22 is value of it

# printing the name and age variable
print(name, age)
# to print more than one value use comma(,) to saperate them

# simple math using print function
print(1+1)
print(23 + 12)

#getting user input using "input" function
myName = input("what is your name? ")
print("hello", myName)
# to print string with some value, saperate them by using comma(,)

# using back slashes we can escape character like \n for new line or next line and \' or \" for adding another quote in a print string
print("this is quotation mark \" \" ")

# using f string we can format the string output of a print function
print(f"this is {myName}'s GitHub Repository")

# Doing basics for maths (+, -, *, /) as calculator
num1 = 12
num2 = 34

result = num1 + num2

print(f"the result of addition is : {result}")

# doing math with user input by using input() function and int() function
no1 = int(input("Enter first number: "))
no2 = int(input("Enter second number: "))
# here's input() will give us a string of but int() will convert it's type into an integer
res = no1 - no2

print(f"the result of substraction is : {res}")

n1 = input("enter a number: ")
n2 = input("enter another number: ")

# we also can convert the type like this.
ans = int(n1) * int(n2)

print(f"the answer of multiplication is : {ans}")

#formatting numbers as currency like 1000 to 1,000 and 100000 to 100,000
# we are using float and not int because number may have been decimel format
number = float(input("enter a big number: "))

#round() function is for rounding up a decimel number to it's closest whole integer number
number = round(number)

#using thsi format of {number:,} we can add comma or period in currency output as country system.
print(f"{number:,}")



# these are the some of the operators that is used by python
# Arithmatic Operator : +, -, *, /, %

# Conditional(Comparison) Operator : <, <=, >, >=, ==, !=

# Logical Operator : and, or, not

