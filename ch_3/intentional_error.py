guests = ['Houdini', 'Tesla', 'Aliens']
print("We found a bigger dinner table.")
guests.insert(0, 'Jobs')
guests.insert(2, 'Openhiemer')
guests.append('Roosevelt')
message = ", you're invited to dinner."
try:
    print(guests[0] + message)
    print(guests[1] + message)
    print(guests[2] + message)
    print(guests[3] + message)
    print(guests[4] + message)
    print(guests[6] + message)
except Exception as e:
    print(e)    
print("I am inviting", len(guests), "guests to dinner")