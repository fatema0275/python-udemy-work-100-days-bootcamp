print("Welcome to tip calculator")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you want to give? 10, 12 or 15?"))
people = int(input("How many people to split the bill? "))
totalBill = bill + ((bill*tip)/100)
answer = totalBill / people
finalAmt = round(answer,2)
print(f"Each person should pay: ${finalAmt}")

