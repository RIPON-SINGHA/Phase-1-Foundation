# Using custom greet module 

from greet import hallo
from greet import goodbye
import sys


# accessing the functions on this condition
if len(sys.argv) == 2:
    hallo(sys.argv[1])
    goodbye(sys.argv[1])
