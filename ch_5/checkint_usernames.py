current_users = ['Admin', 'mattDubbz', 'jessiGiB', 'chadbrochill', 'chazzz', 'new1', 'new2']
new_users = ['New1', 'new2', 'new3', 'new4', 'new5']

# for index, user in enumerate(current_users):
#     current_users[index] = user.lower()
# print(current_users)

current_users = [user.lower() for user in current_users]
new_users = [user.lower() for user in new_users]

for user in new_users:
    if user in current_users:
        print("You'll need to pick another username")
    else:
        print("That username is available.")
