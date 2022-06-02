age = int(input("Input age: "))

# if age < 2:
#     print("You're a baby.")
# elif age < 4:
#     print("You're a toddler.")
# elif age < 13:
#     print("You're a kid.")
# elif age < 20:
#     print("You're a teenager.")
# elif age < 65:
#     print("You're an adult.")
# elif age >= 65:
#     print("You're an elder.")

# if age <= 1:
#     print("You're a baby.")
# elif age <= 3:
#     print("You're a toddler.")
# elif age <= 12:
#     print("You're a kid.")
# elif age <= 19:
#     print("You're a teenager.")
# elif age <= 64:
#     print("You're an adult.")
# elif age >= 65:
#     print("You're an elder.")

if age >= 65:
    print("You're an elder.")
elif age >= 20:
    print("You're an adult.")
elif age >= 13:
    print("You're a teenager.")
elif age >= 4:
    print("You're a kid")
elif age >= 2:
    print("You're a toddler.")
else:
    print("You're a baby.")
