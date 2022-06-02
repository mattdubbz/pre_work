cities = {
    "Dallas": {"country": "US", "population": 7307413, "fact": "Lone Star Stuff"},
    "Aukland": {
        "country": "New Zealand",
        "population": 306743,
        "fact": "Way down under",
    },
    "Paris": {
        "country": "France",
        "population": 4392849,
        "fact": "Antsy in the pantsy",
    },
}
# for city, info in cities.items():
#     print(f"{city}: ")
#     for stat in info:
#         print(f"\t{stat.title()}: {info[stat]}")
#     print("=====================")

for city, info in cities.items():
    print(f"{city}: ")
    for stat, val in info.items():
        print(f"\t{stat.title()}: {val}")
    print("=====================")
