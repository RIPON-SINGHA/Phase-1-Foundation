#sys — System-specific parameters and functions

# This module provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter. It is always available. Unless explicitly noted otherwise, all variables are read-only

# "sys.argv"
# this is another python library or module by which the list of command line arguments passed to a Python script.
# argv[0] is the script name (it is operating system dependent whether this is a full pathname or not).
# If the command was executed using the -c command line option to the interpreter, argv[0] is set to the string '-c'
# If no script name was passed to the Python interpreter, argv[0] is the empty string.


import sys

print("Hello, my name is", sys.argv[1])

# checking how many arguments were passed
num_args = len(sys.argv)

# access the first argument 
if num_args > 1:
    user_args = sys.argv[1]

print(f"Argument recieved: {user_args}")




# we can print multiple given inputs with the sys.argv by using loop
if len(sys.argv) < 2: 
    sys.exit("Too few arguments")

for arg in sys.argv[1:-3]:
    print(f"Hello my name is {arg}" )
