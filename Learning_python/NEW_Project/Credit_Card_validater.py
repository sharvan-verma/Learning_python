"""
1. Remove (-) Dash and Blank spaces 
2. Reverse the card number
3. Add all digits in the odd places from right to left
4. Double every second even digit from right to left
   (If the result is a two-digit number, add the two digits together to get a single digit)
5. Add all the digits
6. If the total is divisible by 10, the card number is valid
"""

sum_odd_digit = 0
sum_even_digit = 0
total = 0

# Step 1: Input and Clean the Card Number
card_number = input("Enter a credit card number #: ")
card_number = card_number.replace("-", "")  # Remove dashes
card_number = card_number.replace(" ", "")  # Remove spaces
card_number = card_number[::-1]  # Reverse the card number
print("Credit card number:", card_number)

# Step 2: Sum of Odd Digits
for x in card_number[::2]:  # Iterate through odd-positioned digits (from right)
    sum_odd_digit += int(x)  # Convert to integer and add to sum

# Step 3: Sum of Doubled Even Digits
for x in card_number[1::2]:  # Iterate through even-positioned digits (from right)
    x = int(x) * 2  # Double the digit
    if x >= 10:  # If the result is a two-digit number
        sum_even_digit += (1 + (x % 10))  # Add the digits together (e.g., 12 becomes 1 + 2 = 3)
    else:
        sum_even_digit += x  # Otherwise, add the doubled digit directly

# Step 4: Calculate Total Sum
total = sum_odd_digit + sum_even_digit

# Step 5: Check Validity
if total % 10 == 0:  # If the total is divisible by 10
    print("Valid credit card number")
else:
    print("Invalid credit card number")

# Display Intermediate Results (for debugging or information)
print("Sum of odd digits:", sum_odd_digit)
print("Sum of even digits:", sum_even_digit)
print("Total:", total)