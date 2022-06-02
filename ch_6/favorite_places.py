favorite_places = {
    "Matt": ["Cocomo", "Jackson Hole", "Telluride"],
    "Jess": ["Cabo", "Florida", "Texas"],
    "Maria": ["Arizona", "Ireland", "Mexico"],
}

for name, places in favorite_places.items():
    print(f"{name}'s favorite places are: ")
    for place in places:
        print(f"\t{place}")
    print("============")
    