print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
age = int(input("What is your age? "))

bill = 0.0

if height >= 120:
    print("You can ride the rollercoaster")
    if age <= 12:
        print("Child tickets are $5")
        bill = bill + 5
    elif age<=18:
        print("Youth tickets are $10")
        bill = bill + 10
    else:
        print("Adult tickets are $12")
        bill = bill + 12

    photo = input("Do you want a picture to be taken when on the ride? ")
    if photo == "yes":
        print("An extra $3 will be added to your bill")
        bill = bill + 3
    else:
        print("No extra charges to be paid, thanks for visiting")
else:
    print("You cannot ride the rollercoaster")

print(f"Your bill is ${bill}")