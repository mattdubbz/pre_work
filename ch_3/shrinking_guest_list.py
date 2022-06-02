guests = ['Houdini', 'Tesla', 'Aliens']
print("We found a bigger dinner table.")
guests.insert(0, 'Jobs')
guests.insert(2, 'Openhiemer')
guests.append('Roosevelt')
message = ", you're invited to dinner."
print("The dinner table won't get here in time, I can only invite 2 guests.")
sorry1 = guests.pop()
print("Sorry", sorry1, "you can't come to dinner now.")
sorry2 = guests.pop()
print("Sorry", sorry2, "you can't come to dinner now.")
sorry3 = guests.pop()
print("Sorry", sorry3, "you can't come to dinner now.")
sorry4 = guests.pop()
print("Sorry", sorry4, "you can't come to dinner now.")
print(guests)
del guests[1]
del guests[0]
print(guests)
