import random

import random

def spin_row():
    symbols = ['🍒', '🍉', '🍋', '🔔', '✨']
    weights = [3, 2, 2, 1, 1]  
    results = random.choices(symbols, weights, k=3) 
    return results


def print_row(row):
    print("********************")
    print(" | ".join(row))
    print("********************")

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍒':
            return bet * 3
        elif row[0] == '🍉':
            return bet * 4
        elif row[0] == '🍋':
            return bet * 5
        elif row[0] == '🔔':
            return bet * 6
        elif row[0] == '✨':
            return bet * 7
    elif row[0] == row[1]:
        return bet * 2
    return 0

def main():
    balance = 100

    print("********************************")
    print("Welcome to Python Slots")
    print("Symbols: 🍒 🍉 🍋 🔔 ✨")
    print("********************************")

    while balance > 0:
        print(f"Current balance: ${balance}")

        bet = input("Please enter your bet amount: ")

        if not bet.isdigit():
            print("Please enter a valid number")
            continue

        bet = int(bet)

        if bet > balance:
            print("Insufficient balance")
            continue

        if bet <= 0:
            print("Bet must be greater than zero.")
            continue

        balance -= bet
        row = spin_row()
        print("Spinning...\n")

        print_row(row)

        payout = get_payout(row, bet)

        if payout > 0:
            print(f"You won ${payout}! 🎉")
            balance += payout
        else:
            print("You lost. 😔")

        if balance <= 0:
            print("Game over. You're out of money.")
            break

        play_again = input("Play again? (y/n): ").lower()
        if play_again != "y":
            break

if __name__ == "__main__":
    main()