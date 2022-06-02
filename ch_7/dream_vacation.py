responses = {}
active = True
while active:
    vaca = input("Where do you want to vaca? ")
    name = input("What is your name? ")
    responses[name] = vaca
    repeat = input("Do you want to poll again?")
    if repeat == 'no':
        active = False

for name, vaca in responses.items():
    print("----Poll Results----")
    print(f"{name.title()}: {vaca.title()}")
