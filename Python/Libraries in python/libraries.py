# In python there is multiple libraries and modules to use as per needs.
# libraries and modules are created by other and used by everyone so we can use those programs or modules or functions without coding it in our project.
# To use module we need to first import that module or library in our python code using the keyword "import"
# and then we can use any methods or function of that exact module or library we imported at first

# import random

# toss = random.choice(["Heads", "Tails"])
# print(toss)

# random library is used to get some random value from using choice() function
# it will give us the random value from the argumets of the choice() function







from random import choice

coin = choice(["Heads", "Tails"])
print(coin)

# we also can import the exact function or method we need from one library or module using "from" keyword
# using "from" keyword we can only import one function or method from a library at a time if we dont need any others. But this is not good practice to do like that,
# so we use only "import" as we can use every functions from one line of code.





import random

number = random.randint(1, 50)
print(number)

# randint() is a fucntion in comes with "random" library which gives us the random number integer between the two value are given. 




cars = ["Bugatti", "Farrari", "Lamborgini", "Corvette"]
random.shuffle(cars)
for car in cars:
    print(car)

# shuffle() is another function which shuffles the list of values with its place. shuffle works for list of value not single valued list or any single value




# python has a library or module called "statistics" by means it can provide functions for calculating methametical statistics of numeric data

import statistics

print(statistics.mean([100, 90]))