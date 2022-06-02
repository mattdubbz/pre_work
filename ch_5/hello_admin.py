usernames = ['admin', 'mattdubbz', 'jessibig', 'chadbrochill', 'chazzz']

for username in usernames:
    if username == 'admin':
        print("Hello admin, would you like to see a status report?")
        continue
    print(f"Hello {username}, thank you for logging in again.")
