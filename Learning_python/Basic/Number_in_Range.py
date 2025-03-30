def check_number_range(number, lower_bound, upper_bound):
    """Checks if a number is within a given range (inclusive)."""

    if lower_bound <= number <= upper_bound:
        return "Number is within the range."
    else:
        return "Number is outside the range."

# Example usage:
num = float(input("Enter a number: "))
lower = float(input("Enter the lower bound: "))
upper = float(input("Enter the upper bound: "))

result = check_number_range(num, lower, upper)
print(result)




