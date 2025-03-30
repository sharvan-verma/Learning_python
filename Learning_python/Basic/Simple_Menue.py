# 18. Simple Menu
def simple_menu():
    """Creates a simple menu with options and performs actions."""
    print("Menu:")
    print("1. Breakfastet")
    print("2. Exit")

    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        print("Dosa")
        print("Maggie")
        print("Bread Jam")
        print("Juice")
        print("Samosa")
        print("Milk")
        print("Pizza")

    elif choice == "2":
        print("Goodbye!")
    else:
        print("Invalid choice.")

# Example:
simple_menu()


