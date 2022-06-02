rivers = {'nile': 'egypt', 'cuyahoga': 'ohio', 'rio grande': 'texas'}
for river, location in rivers.items():
    print(f"The {river} river is in {location}.")

for river in rivers.keys():
    print(f"River name: {river}")

for location in rivers.values():
    print(f"River location: {location}")
    