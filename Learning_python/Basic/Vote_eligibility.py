def check_voting_eligibility(age):
    """Checks if a person is eligible to vote based on their age."""

    if not isinstance(age, int):
        return "Invalid input. Age must be an integer."

    if age < 0:
        return "Invalid input. Age cannot be negative."

    voting_age = 18  # Minimum voting age

    if age >= voting_age:
        return "Eligible to vote."
    else:
        return "Not eligible to vote."

# Example usage:
person_age = int(input("Enter the person's age: "))
eligibility = check_voting_eligibility(person_age)
print(eligibility)