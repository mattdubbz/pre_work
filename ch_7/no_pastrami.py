sandwich_orders = [
    "sub",
    "panini",
    "pastrami",
    "giant sub",
    "pastrami",
    "mega sub",
    "party sub",
    "gyro",
    "pastrami",
]
print("The deli has ran out of pastrami.")
while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

finished_sandwiches = []
while sandwich_orders:
    samy = sandwich_orders.pop()
    print(f"I made your {samy}!")
    finished_sandwiches.append(samy)
print(sandwich_orders)
print(finished_sandwiches)
