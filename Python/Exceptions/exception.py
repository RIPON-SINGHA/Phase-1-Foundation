#ValueError:

try:
    num = int(input("Enter a number: "))
    print(f"number is {num}")
except ValueError:
    print("you should not give a string here! FBI is approaching your home right now for this fatel mistake...")


#NameError: with using "else" keyword
# A program can have multiple errors so we use else if any of them are valid now that instance.

try:
    x = int(input("Enter a number: "))
except ValueError:
    print("Enter a number, not a string!")
else:
    print(f"number is {x}")


# using loop for continuous input if Error is found

while True:
    try:
        z = int(input("Enter a number: "))
    except ValueError:
        print("Enter a number you dummy stupic baka!")
    else:
        break
        # print(f"z is {z}")

print(f"z is {z}")




# using function creating same logic:

def main():
    x = get_int()
    print(f"x is {x}")


def get_int():

    while True:
        try:
            x = int(input("Enter a number: "))
        except ValueError:
            print("Enter a number you dumbAss!")
        else:
            return x   

main()



# we can use "except" statement without giving any hint or error direction. we can pass the error and start with the loop using "pass" keyword

def main():
    x = get_int()
    print(f"x is {x}")


def get_int():

    while True:
        try:
            x = int(input("Enter a number: "))
            return x
        except ValueError:
            pass
    
main()



# Another way to impliment this using arguments in functions
def main():
    x = get_int("Enter a number: ")
    print(f"x is {x}")


def get_int(Input):

    while True:
        try:
            x = int(input(Input))
            return x
        except ValueError:
            pass
    
main()
