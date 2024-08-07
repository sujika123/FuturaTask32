# Write a function called square that takes a number as an argument and returns its square.
# Include a docstring that explains the purpose of the function.


def square(number):
    """
    Calculate the square of a number.

    Args:
        number (int or float): The number to be squared.

    Returns:
        int or float: The square of the input number.
    """
    return number ** 2


num = 7  # You can change this number to test with other values
result = square(num)
print(f"The square of {num} is: {result}")

