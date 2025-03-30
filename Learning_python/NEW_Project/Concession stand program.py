menu = {
    "pizza": 3.00,
    "nachos": 4.50,
    "popcorn": 6.00,
    "fries": 2.50,
    "chips": 1.00,
    "soda": 3.00,
    "lemonade": 4.25,
}

cart = []
total = 0

print("----------- MENU --------------")
for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")

print("-------------------------")

while True:
    food = input("Select an item (q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
        print("-------------------------")
        total = 0 #reset total each time, to avoid double counting.
        for item in cart:
            total += menu.get(item)
    else:
        print("Invalid item.")

print("------ YOUR CART ------")
for item in cart:
    print(f"{item:10}: ${menu[item]:.2f}")

print(f"Total: ${total:.2f}")