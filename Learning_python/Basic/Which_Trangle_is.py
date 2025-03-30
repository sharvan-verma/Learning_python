def triangle_type(side1, side2, side3):
    """Determines the type of triangle given three sides."""

    if not (isinstance(side1, (int, float)) and isinstance(side2, (int, float)) and isinstance(side3, (int, float))):
        return "Invalid input. Sides must be numeric."

    if not (side1 > 0 and side2 > 0 and side3 > 0):
        return "Invalid input. Sides must be positive."

    if not (side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1):
        return "Invalid input. These sides cannot form a triangle."

    if side1 == side2 == side3:
        return "Equilateral"
    elif side1 == side2 or side1 == side3 or side2 == side3:
        return "Isosceles"
    else:
        return "Scalene"

# Example usage:
side_a = float(input("Enter side 1: "))
side_b = float(input("Enter side 2: "))
side_c = float(input("Enter side 3: "))

result = triangle_type(side_a, side_b, side_c)
print(result)