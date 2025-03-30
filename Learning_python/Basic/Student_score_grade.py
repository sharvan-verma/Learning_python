def grade_calculator(score):
    """Calculates and returns the grade based on the student's score."""

    if not isinstance(score, (int, float)):
        return "Invalid input. Score must be a number."

    if score < 0 or score > 100:
        return "Invalid input. Score must be between 0 and 100."

    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

# Example usage:
student_score = float(input("Enter the student's score: "))
grade = grade_calculator(student_score)
print(f"The student's grade is: {grade}")
