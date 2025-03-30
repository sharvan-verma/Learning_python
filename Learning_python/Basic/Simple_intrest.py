# 20. Simple Interest
def simple_interest(principal, rate, time):
    """Calculates simple interest."""
    return (principal * rate * time) / 100

# Example:
principal_amount = float(input("Enter principal amount: "))
interest_rate = float(input("Enter interest rate (in percentage): "))
time_period = float(input("Enter time period (in years): "))
interest = simple_interest(principal_amount, interest_rate, time_period)
print(f"Simple interest: {interest}")

