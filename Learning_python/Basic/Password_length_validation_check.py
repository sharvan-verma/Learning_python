def validate_password(password):
    """Checks if a password is at least 8 characters long."""

    if not isinstance(password, str):
        return "Invalid input. Password must be a string."

    if len(password) >= 8:
        return "Valid password."
    else:
        return "Invalid password. Password must be at least 8 characters long."

# Example usage:
password_input = input("Enter a password: ")
validation_result = validate_password(password_input)
print(validation_result)



