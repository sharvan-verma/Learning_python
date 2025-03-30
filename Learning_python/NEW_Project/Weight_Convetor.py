weight = float(input("Enter your weight: "))
unit = input("Kilogram or Pounds? (K or P): ")

if unit.upper() == "K":
    weight = weight * 2.205
    unit = "LBS."
elif unit.upper() == "":
    weight = weight / 2.205
    unit = "Kgs"
else:
    print(f"{unit} was not valid")
    exit()

print(f"Your weight is: {weight:.2f} {unit}")