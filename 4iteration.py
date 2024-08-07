#4.Write a program to iterate the first 10 numbers, and in each
#iteration, print the sum of the current and previous number.


def iterate_and_sum():
    previous_number = 0

    for current_number in range(10):
        sum_numbers = previous_number + current_number
        print(f"Current Number: {current_number}, Previous Number: {previous_number}, Sum: {sum_numbers}")
        previous_number = current_number

# Run the function
iterate_and_sum()



#Method 2

# Initialize the previous number
previous = 0

# Iterate the first 10 numbers
for i in range(1, 11):
    # Print the sum of the current and previous number
    print(f"Current: {i}, Previous: {previous}, Sum: {i + previous}")

    # Update the previous number for the next iteration
    previous = i