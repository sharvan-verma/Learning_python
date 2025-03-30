import math

def calculate_compound_interest(principal, rate, time):
  
    """ Calculates compound interest.  """

    # Validate inputs
    if principal <= 0:
        raise ValueError("Principal amount must be greater than zero.")
    if rate <= 0:
        raise ValueError("Annual interest rate must be greater than zero.")
    if time <= 0:
        raise ValueError("Time period must be greater than zero.")

    # Calculate compound interest
    amount = principal * math.pow((1 + rate / 100), time)
    ci = amount - principal
    return ci

while True:
    try:
        principal = float(input("Enter the principal amount: "))
        if principal <= 0:
            raise ValueError
        break
    except ValueError:
        print("Invalid principal. Enter a value greater than zero.")

while True:
    try:
        rate = float(input("Enter the annual interest rate (in percentage): "))
        if rate <= 0:
            raise ValueError
        break
    except ValueError:
        print("Invalid rate. Enter a value greater than zero.")

while True:
    try:
        time = float(input("Enter the number of years: "))
        if time <= 0:
            raise ValueError
        break
    except ValueError:
        print("Invalid time. Enter a value greater than zero.")

try:
    compound_interest = calculate_compound_interest(principal, rate, time)
    print("Compound Interest:", compound_interest)
except ValueError as e:
    print(f"Error: {e}")