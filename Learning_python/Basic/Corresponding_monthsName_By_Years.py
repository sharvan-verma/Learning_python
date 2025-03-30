def month_name(month_number):
    """
    Takes a number (1-12) as input and returns the corresponding month name.

    Args:
      month_number: An integer between 1 and 12.

    Returns:
      The name of the month as a string.
      Returns "Invalid input" if the month_number is not within the valid range.
    """
    months = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }

    if 1 <= month_number <= 12:
        return months[month_number]
    else:
        return "Invalid input"

# Example usage:
month_number = int(input("Enter a number (1-12): "))
month = month_name(month_number)
print(month)