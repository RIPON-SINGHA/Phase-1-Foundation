# this is a custom library that greet the user hallo and goodbye
# module has two functions hallo() and goodbye() and one main() function
# when i use it as a module main() fucntion wont run because then the value of __name__ would be different.

def main():
    hallo("World")
    goodbye("World")


def hallo(name):
    print(f"Hallo, {name}")


def goodbye(name):
    print(f"GoodBye, {name}")


# to verify that main() fucntio is not being called when used as a module and only work when this file is being compiled
# when this code is being accessed as a module, "__name__" is not set to __main__ and that's why the main() function wont work there but only source code compilation
if __name__ == "__main__":
    main()