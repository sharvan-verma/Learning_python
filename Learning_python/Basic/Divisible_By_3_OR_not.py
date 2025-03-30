def divisible_by_3_and_5(number):
    """Checks if a number is divisible by both 3 and 5."""
    if number % 3 == 0 and number % 5 == 0:
        return True
    else:
        return False