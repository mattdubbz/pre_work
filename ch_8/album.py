from os import NGROUPS_MAX


def make_album(name, title, num_tracks=""):
    album = {"name": name, "title": title}
    if num_tracks:
        album["tracks"] = num_tracks
    return album


print(make_album("Blink-182", "Take Off Your Pants and Jacket"))
print(make_album("Led Zeppelin", "Mothership"))
print(make_album("Ace Marino", "Cocaine Flamingo"))
print(make_album("Ace Marino", "Digital Memories", "10"))
