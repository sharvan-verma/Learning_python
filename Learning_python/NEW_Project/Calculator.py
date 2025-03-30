def calculator():
    """Takes two numbers and performs basic arithmetic operations."""

    num1 = float(input("Enter Num1: "))
    num2 = float(input("Enter Num2: "))
    operator = input("Enter an operator (+, -, *, /): ")

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
            return
        result = num1 / num2
    else:
        print("Invalid Operator.")
        return

    print("Result:", result)

calculator()

