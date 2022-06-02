sandwich_orders = ["sub", "panini", "giant sub", "mega sub", "party sub", "gyro"]
finished_sandwiches = []
while sandwich_orders:
    samy = sandwich_orders.pop()
    print(f"I made your {samy}!")
    finished_sandwiches.append(samy)
print(sandwich_orders)
print(finished_sandwiches)
