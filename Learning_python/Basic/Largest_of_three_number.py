numA = int(input("enter a number: "))
numB = int(input("enter a number: "))
numC = int(input("enter a number: "))

if numA >= numB and numA >= numC:
  print("numA is greater")
elif numB >= numA and numB >= numC:  
  print("numB is greater")
else:
  print("numC is greater")

