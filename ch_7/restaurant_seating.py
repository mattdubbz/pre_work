num_people = int(input("How many people are in your dining group? "))
if num_people > 8:
    print("You'll have to wait.")
else:
    print("I have a table for", num_people, "people ready right now.")
