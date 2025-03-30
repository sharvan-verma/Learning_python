import tkinter as tk
from tkinter import messagebox

balance = 0.0

def show_balance():
    messagebox.showinfo("Balance", f"Your balance is ${balance:.2f} 💰")

def deposit():
    global balance
    try:
        amount = float(deposit_entry.get())
        if amount > 0:
            balance += amount
            messagebox.showinfo("Deposit", f"${amount:.2f} deposited successfully! 🎉")
            show_balance()
        else:
            messagebox.showerror("Error", "Invalid deposit amount. 🚫")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number. 🔢")

def withdraw():
    global balance
    try:
        amount = float(withdraw_entry.get())
        if 0 < amount <= balance:
            balance -= amount
            messagebox.showinfo("Withdrawal", f"${amount:.2f} withdrawn successfully! 💸")
            show_balance()
        else:
            messagebox.showerror("Error", "Insufficient funds or invalid withdrawal amount. ❌")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number. 🔢")

def exit_program():
    if messagebox.askyesno("Exit", "Are you sure you want to exit? 👋"):
        root.destroy()

# GUI Setup
root = tk.Tk()
root.title("🏦 Python Banking Program 🏦")

# Make window bigger
root.geometry("400x300")  # Adjust size as needed

# Center window
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

window_width = 400  # Same as geometry
window_height = 300 # Same as geometry

x = (screen_width / 2) - (window_width / 2)
y = (screen_height / 2) - (window_height / 2)

root.geometry(f"{window_width}x{window_height}+{int(x)}+{int(y)}") 

# Labels
tk.Label(root, text="Welcome to the Banking Program! 🌟", font=("Arial", 14)).pack(pady=10)

# Deposit section
tk.Label(root, text="Deposit Amount: $").pack()
deposit_entry = tk.Entry(root)
deposit_entry.pack()
tk.Button(root, text="Deposit 💰", command=deposit).pack(pady=5)

# Withdraw section
tk.Label(root, text="Withdraw Amount: $").pack()
withdraw_entry = tk.Entry(root)
withdraw_entry.pack()
tk.Button(root, text="Withdraw 💸", command=withdraw).pack(pady=5)

# Buttons
tk.Button(root, text="Show Balance 📊", command=show_balance).pack(pady=5)
tk.Button(root, text="Exit 👋", command=exit_program).pack(pady=10)

root.mainloop()

print("Thank you, have a nice day! 😊")