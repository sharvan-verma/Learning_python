def check_character_type(char):
    """Checks if a character is uppercase, lowercase, or a digit."""

    if not isinstance(char, str) or len(char) != 1:
        return "Invalid input. Please enter a single character."

    if char.isupper():
        return "Uppercase"
    elif char.islower():
        return "Lowercase"
    elif char.isdigit():
        return "Digit"
    else:
        return "Special Character"

# Example usage:
character = input("Enter a character: ")
result = check_character_type(character)
print(result)