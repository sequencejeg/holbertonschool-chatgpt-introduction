#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a given non-negative integer n.

    Function Description:
    Computes the factorial of a non-negative integer using recursion.

    Parameters:
    n (int): A non-negative integer for which the factorial is to be computed.
    
    Returns:
    int: The factorial of the input integer n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Check if a command-line argument is provided
if len(sys.argv) != 2:
    print("Usage: python3 factorial.py <number>")
    sys.exit(1)

try:
    # Convert the command-line argument to an integer
    number = int(sys.argv[1])
    
    # Ensure the number is non-negative
    if number < 0:
        raise ValueError("The number must be a non-negative integer.")

    # Compute the factorial of the number
    f = factorial(number)
    
    # Print the result
    print(f)

except ValueError as e:
    # Handle errors related to invalid input
    print(e)
    print("Please enter a valid non-negative integer.")
