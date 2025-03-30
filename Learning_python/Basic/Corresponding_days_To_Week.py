def day_of_week(day_number):
    """
    Takes a number (1-7) as input and returns the corresponding day of the week.

    Args:
      day_number: An integer between 1 and 7.

    Returns:
      The name of the day of the week as a string.
      Returns "Invalid input" if the day_number is not within the valid range.
    """
    days_of_week = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
    }

    if 1 <= day_number <= 7:
        return days_of_week[day_number]
    else:
        return "Invalid input"

# Example usage:
day_number = int(input("Enter a number (1-7): "))
day = day_of_week(day_number)
print(day)