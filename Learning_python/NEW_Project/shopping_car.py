food = []
prices = []  # Changed "price" to "prices" to avoid confusion
total = 0

while True:
    item = input("Enter a food to buy (q to quit): ")
    if item.lower() == "q":
        break
    else:
        try:
            price = float(input(f"Enter the price of {item}: $"))
            food.append(item)
            prices.append(price)
        except ValueError:
            print("Invalid price. Please enter a numerical value.")

print("------ YOUR CART ------")

for i in range(len(food)):
    print(f"{food[i]}: ${prices[i]:.2f}")  # formatted printing

for price in prices:
    total += price

print(f"Your total is: ${total:.2f}") #formatted total.