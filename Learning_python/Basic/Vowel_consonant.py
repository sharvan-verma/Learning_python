def vowel_or_consonant(char):
    """Determines if a character is a vowel or consonant."""

    char = char.lower()  # Convert to lowercase for easier comparison

    if len(char) != 1 or not char.isalpha():
        return "Invalid input. Please enter a single alphabet character."

    vowels = "aeiou"

    if char in vowels:
        return "Vowel"
    else:
        return "Consonant"

# Example usage:
character = input("Enter a character: ")
result = vowel_or_consonant(character)
print(result)