# 19. Temperature Conversion
def temperature_conversion():
    """Converts Celsius to Fahrenheit or vice versa."""
    print("Temperature Conversion:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")

    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius} Celsius is {fahrenheit} Fahrenheit.")
    elif choice == "2":
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5/9
        print(f"{fahrenheit} Fahrenheit is {celsius} Celsius.")
    else:
        print("Invalid choice.")

# Example:
temperature_conversion()