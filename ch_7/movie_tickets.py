age = int(input("Enter your age for you ticket price or 999 to quit: "))
while age != 999:
    price = 0
    if age < 3:
        price = 0
    elif age < 13:
        price = 10
    else:
        price = 15
    if price == 0:
        print("You're ticket is free!")
    else:
        print(f"Your ticket price is ${price}.")
    age = int(input("Enter your age for you ticket price or 999 to quit: "))
