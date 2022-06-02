def make_album(name, title, num_tracks=""):
    album = {"name": name.title(), "title": title.title()}
    if num_tracks:
        album["tracks"] = num_tracks
    return album


while True:
    print("Enter the album info or enter 'q' to quit at any time.")
    name = input("Artists's name: ")
    if name.lower() == "q":
        break
    title = input("Album title: ")
    if title.lower() == "q":
        break
    num_tracks = input("Number of tracks (Optional): ")
    if num_tracks.lower() == "q":
        break
    print(make_album(name, title, num_tracks))
