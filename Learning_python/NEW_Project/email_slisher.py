email = input("Enter your email: ")
try:
    index = email.index("@")
    username = email[:index]
    domain = email[index +1:]
    print(f"Your username is {username} and domain is {domain}")
except ValueError:
    print("Invalid email format: '@' not found.")
    exit()