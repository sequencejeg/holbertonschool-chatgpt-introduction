#!/usr/bin/python3
import sys

def factorial(n):
    if n == 0 or n == 1:
        return 1
    result = 1
    while n > 1:
        result *= n
        n -= 1  # Decrement n to avoid an infinite loop
    return result

# Ensure an argument is passed
if len(sys.argv) < 2:
    print("Error: Please provide a number as a command-line argument.")
    sys.exit(1)

try:
    number = int(sys.argv[1])
    if number < 0:
        print("Error: Factorial is not defined for negative numbers.")
    else:
        f = factorial(number)
        print(f)
except ValueError:
    print("Error: Please provide a valid integer.")
