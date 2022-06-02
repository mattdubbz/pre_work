languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
    "alex": "go",
    "james": "swift",
    "john": "php",
}

taken = ["edward", "james", "sarah"]

for name in languages.keys():
    if name in taken:
        print(f"{name.title()}, thanks for taking the poll!")
    else:
        print(f"{name.title()}, please take the poll.")
