def show_magicians(magicians):
    for i in range(len(magicians)):
        magicians[i] = "The Great " + magicians[i]
        print(magicians[i].title())


magicians = ["Houdini", "Von Bron", "Harry", "Woz", "Oz"]
show_magicians(magicians)
print(magicians)
