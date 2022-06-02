from copy import copy


def show_magicians(magicians):
    for i in range(len(magicians)):
        magicians[i] = "The Great " + magicians[i]
        print(magicians[i].title())
    return magicians


magicians = ["Houdini", "Von Bron", "Harry", "Woz", "Oz"]
copy_list = show_magicians(magicians[:])
print(copy_list)
print(magicians)
