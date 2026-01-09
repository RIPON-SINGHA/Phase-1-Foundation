# defining a function for a simple calculation which will return a value of the result of the addition
def calculator(num1, num2):
    return num1 + num2

num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))

# we can use function calls inside print function and also add parameters in it
print(f"the answer is : {calculator(num1, num2)}")




# defining two function main() and square() to calculate the square root of a number
def main():
    n = int(input("enter a number pls: "))
    print(f"the square root of the number is: {sqrt(n)} ")

# returning a value of square of the given number
def sqrt(num):
    return num * num

main() # calling the main() function


# different ways of powering a number:
print(2 * 2)
print(3 ** 2) # using double asterisk ** will multiply the number the given times. here 3 is multiplied 2 times
print(pow(4, 2)) # using pow() we can calculate a number's square root or its cube with the second parameter. pow(4, 2) is 4 * 4 and pow(4, 3) is 4 * 4 * 4