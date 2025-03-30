#Take a number as input and print its sign.

Check_Pos_Neg_Zero = int(input("Enter a Pos(+), Neg(-), and Zero(0) Numbers: "))

if Check_Pos_Neg_Zero == 0:
    print("Zero(0)")

elif Check_Pos_Neg_Zero <= -1:
    print("Neg(-)")
else:
    print("Pos(+)")

