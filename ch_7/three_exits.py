# topping = ''
# while topping != 'quit':
#     topping = input("Enter a topping for your pizza: ")
#     if topping == 'quit':
#         break
#     else:
#         print(f"I'll add {topping} to the pizza.")

# topping = input("Enter a topping for your pizza: ")
# while topping != 'quit':
#     print(f"I'll add {topping} to the pizza.")
#     topping = input("Enter a topping for your pizza: ")

active = True
while active:
    topping = input("Enter a topping for your pizza or 'quit' to exit: ")
    if topping == 'quit':
        break
    print(f"I'll add {topping} to the pizza.")
    topping = input("Enter a topping for your pizza or 'quit' to exit: ")
